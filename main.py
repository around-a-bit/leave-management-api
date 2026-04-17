from fastapi import FastAPI, HTTPException
import json
from datetime import date
from threading import Lock

app = FastAPI()

DB_FILE = "database.json"
lock = Lock()

# ================= UTIL =================

def read_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def response(success, message, data=None):
    return {
        "success": success,
        "message": message,
        "data": data
    }

def get_next_id(items, key):
    if not items:
        return 1
    return max(item[key] for item in items) + 1

# ================= EMPLOYEES =================

@app.get("/api/employees")
def get_employees():
    db = read_db()
    return response(True, "All employees", db["employees"])


@app.get("/api/employees/{id}")
def get_employee(id: int):
    db = read_db()
    emp = next((e for e in db["employees"] if e["employeeId"] == id), None)
    if not emp:
        raise HTTPException(404, "Employee not found")
    return response(True, "Employee found", emp)


@app.post("/api/employees")
def create_employee(emp: dict):
    with lock:
        db = read_db()

        emp["employeeId"] = get_next_id(db["employees"], "employeeId")
        db["employees"].append(emp)

        write_db(db)

    return response(True, "Employee created", emp)


@app.put("/api/employees/{id}")
def update_employee(id: int, updated: dict):
    with lock:
        db = read_db()

        emp = next((e for e in db["employees"] if e["employeeId"] == id), None)
        if not emp:
            raise HTTPException(404, "Employee not found")

        emp.update(updated)

        write_db(db)

    return response(True, "Employee updated", emp)


# ================= LEAVES =================

@app.post("/api/leaves")
def apply_leave(leave: dict):
    with lock:
        db = read_db()

        start = date.fromisoformat(leave["startDate"])
        end = date.fromisoformat(leave["endDate"])
        days = (end - start).days + 1

        balance = next(
            (b for b in db["leave_balances"]
             if b["employeeId"] == leave["employeeId"]
             and b["leaveType"] == leave["leaveType"]
             and b["year"] == start.year),
            None
        )

        if not balance or (balance["totalLeaves"] - balance["usedLeaves"]) < days:
            raise HTTPException(status_code=400, detail="Not enough leave balance")

        leave["leaveId"] = get_next_id(db["leaves"], "leaveId")
        leave["status"] = "Pending"

        db["leaves"].append(leave)
        balance["usedLeaves"] += days

        write_db(db)

    return response(True, "Leave applied", leave)


@app.get("/api/leaves/employee/{id}")
def get_leaves(id: int, status: str = None):
    db = read_db()

    leaves = [l for l in db["leaves"] if l["employeeId"] == id]

    if status:
        leaves = [l for l in leaves if l["status"].lower() == status.lower()]

    return response(True, "Employee leaves", leaves)


# ================= STATUS UPDATE =================

@app.put("/api/leaves/{leaveId}/status")
def update_leave_status(leaveId: int, status: str):
    if status not in ["Approved", "Rejected"]:
        raise HTTPException(400, "Invalid status")

    with lock:
        db = read_db()

        leave = next((l for l in db["leaves"] if l["leaveId"] == leaveId), None)
        if not leave:
            raise HTTPException(404, "Leave not found")

        leave["status"] = status

        write_db(db)

    return response(True, "Leave status updated", leave)


# ================= BALANCE =================

@app.get("/api/leavebalances/employee/{id}/year/{year}")
def get_balance(id: int, year: int):
    db = read_db()

    data = [
        b for b in db["leave_balances"]
        if b["employeeId"] == id and b["year"] == year
    ]

    return response(True, "Leave balances", data)


# ================= VALIDATION =================

@app.post("/api/leave/check")
def check_leave_balance(data: dict):
    db = read_db()

    start = date.fromisoformat(data["startDate"])
    end = date.fromisoformat(data["endDate"])
    days = (end - start).days + 1

    balance = next(
        (b for b in db["leave_balances"]
         if b["employeeId"] == data["employeeId"]
         and b["leaveType"] == data["leaveType"]
         and b["year"] == start.year),
        None
    )

    if not balance:
        return response(False, "No balance record found")

    available = balance["totalLeaves"] - balance["usedLeaves"]

    return response(True, "Validation result", {
        "requested_days": days,
        "available_days": available,
        "can_apply": available >= days
    })