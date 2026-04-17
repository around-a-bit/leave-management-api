````md
# Leave Management System (FastAPI)

## About this project
This is a simple backend API built using FastAPI to manage employee leave data.

It allows:
- Creating and updating employees
- Applying for leave
- Checking leave balance
- Approving or rejecting leave requests

Instead of using a database, this project stores everything inside a `database.json` file.

---

## Tech used
- Python (3.10+)
- FastAPI
- Uvicorn
- JSON file (acts like a database)

---

## 🧰 What you need before running
Make sure you have:
- Python installed (version 3.10 or above)
- Internet connection (for installing packages)

To check Python:
```bash
python --version
````

---

## 🚀 How to run the project (Step-by-step)

### Step 1: Open the project folder

Go to the folder where your project is stored.

Example:

```bash
cd leave_management
```

---

### Step 2: Install required packages

Run this command:

```bash
pip install -r requirements.txt
```

This installs FastAPI and Uvicorn.

---

### Step 3: Start the server

Run this:

```bash
python -m uvicorn main:app --reload
```

---

### Step 4: Open the API in browser

After running, open this in your browser:

```bash
http://127.0.0.1:8000/docs
```

You will see a UI where you can test all APIs.

---

## 📄 API Endpoints (Simple understanding)

### Employees

* Get all employees → `GET /api/employees`
* Get one employee → `GET /api/employees/{id}`
* Add employee → `POST /api/employees`
* Update employee → `PUT /api/employees/{id}`

---

### Leaves

* Apply leave → `POST /api/leaves`
* Get employee leaves → `GET /api/leaves/employee/{id}`
* Approve/Reject leave → `PUT /api/leaves/{leaveId}/status`

---

### Leave Balance

* Get balance → `GET /api/leavebalances/employee/{id}/year/{year}`

---

### Validation

* Check if leave is allowed → `POST /api/leave/check`

---

## 📁 Project structure

```
leave_management/
│
├── main.py          # Main API code
├── database.json    # Stores all data
├── requirements.txt # Dependencies
└── README.md        # Instructions
```

---

## ⚠️ Important notes

* Do not delete `database.json`, it stores all data.
* Data will update automatically when APIs are used.
* If the server stops, just run the start command again.

---

## 🌐 Running this project online (Railway)

1. Push your code to GitHub
2. Go to [https://railway.app](https://railway.app)
3. Create new project → Deploy from GitHub
4. Add this start command:

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

5. After deployment, open:

```
https://your-app.up.railway.app/docs
```

---

## ✅ Do
