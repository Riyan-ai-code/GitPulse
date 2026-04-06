# GitPulse
GitPulse is a real-time team visibility tool for software developers. It monitors what every developer is working on, detects potential merge conflicts before they happen, uses AI to explain the intent behind each code push, and automatically creates Jira issues when conflicts are detected all visible from a live web dashboard and a VS extension.

## Folder Structure

### Backend
```
backend/
├── .env
├── main.py
├── venv/
└── __pycache__/
```

### Docs
```
docs/
```

### Extensions
```
extensions/
```

### Frontend
```
frontend/
├── .--/
└── package.json
```

## How to Run

### Backend
1. Navigate to the `backend` directory.
2. Activate the virtual environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux).
3. Install dependencies if needed: `pip install fastapi uvicorn`.
4. Run the server: `uvicorn main:app --reload`.
5. The API will be available at `http://localhost:8000`.

### Frontend
1. Navigate to the `frontend/.--` directory.
2. Install dependencies: `npm install`.
3. Run the development server: `npm run dev`.
4. The app will be available at `http://localhost:5173`.

### Docs
No setup required - documentation folder is currently empty.

### Extensions
No setup required - extensions folder is currently empty.
