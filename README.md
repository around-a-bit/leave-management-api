```md
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

## What you need before running
Make sure you have:
- Python installed (version 3.10 or above)
- Internet connection (for installing packages)

To check Python:
```

python --version

```

---

## How to run the project (Step-by-step)

### Step 1: Open the project folder
Go to the folder where your project is stored.

Example:
```

cd leave_management

```

---

### Step 2: Install required packages
Run this command:
```

pip install -r requirements.txt

```

This installs FastAPI and Uvicorn.

---

### Step 3: Start the server
Run this:
```

python -m uvicorn main:app --reload

```

---

### Step 4: Open the API in browser
After running, open this in your browser:
```

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

```

You will see a UI where you can test all APIs.

---

## API Endpoints (Simple understanding)

### Employees
- GET /api/employees → Get all employees
- GET /api/employees/{id} → Get one employee
- POST /api/employees → Add employee
- PUT /api/employees/{id} → Update employee

---

### Leaves
- POST /api/leaves → Apply leave
- GET /api/leaves/employee/{id} → Get employee leaves
- PUT /api/leaves/{leaveId}/status → Approve/Reject leave

---

### Leave Balance
- GET /api/leavebalances/employee/{id}/year/{year} → Get leave balance

---

### Validation
- POST /api/leave/check → Check if leave is allowed

---

## Project structure
```

leave_management/
│
├── main.py          # Main API code
├── database.json    # Stores all data
├── requirements.txt # Dependencies
└── README.md        # Instructions

```

---

## Important notes
- Do not delete `database.json`, it stores all data.
- Data will update automatically when APIs are used.
- If the server stops, just run the start command again.

---

## Running this project online (Railway)

1. Push your code to GitHub
2. Go to https://railway.app
3. Create new project → Deploy from GitHub
4. Add this start command:
```

uvicorn main:app --host 0.0.0.0 --port $PORT

```
5. After deployment, open:
```

[https://your-app.up.railway.app/docs](https://your-app.up.railway.app/docs)

```

---

## Final check before submission
- API is running locally
- /docs is opening
- All endpoints are working
- database.json has 5 employees and 15 balance records
- GitHub repo is uploaded
- Live API link is working

---

## Done
If everything above works, your project is ready for submission.
```

---
