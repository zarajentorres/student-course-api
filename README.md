# Student Course API

A small **read-only REST API** built with **Python + Flask** for **Laboratory Activity 3A — System Integration and Architecture**.

The API serves five fictional university courses that are stored directly inside `app.py`. There is **no database**, **no authentication**, and **no write operation** (no POST, PUT, PATCH, or DELETE).

---

## 1. Project overview

| Item | Value |
| --- | --- |
| Project name | Student Course API |
| Type | Standalone backend REST API |
| Data storage | Hard-coded Python list inside `app.py` |
| Allowed HTTP method | `GET` only |
| Database | None (not connected, not claimed) |
| Authentication | None |
| Production server | Gunicorn |

---

## 2. Technologies used

| Technology | Role |
| --- | --- |
| **Python** | Programming language of the backend |
| **Flask** | Web framework that defines the API routes |
| **Flask-CORS** | Allows cross-origin requests for classroom demonstrations |
| **Gunicorn** | Production WSGI server used by Render |
| **GitHub** | Stores the source code |
| **Render** | Hosts the running API as a Web Service |

---

## 3. Project structure

```
student_course_api/
├── app.py            # The whole API: Flask app, course data, routes, errors
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── .gitignore        # Keeps venv/ and __pycache__/ out of GitHub
```

---

## 4. API endpoints

### 4.1 Health check

| | |
| --- | --- |
| Method | `GET` |
| URL | `/api/health` |
| Success | `200 OK` |

```json
{
  "status": "success",
  "message": "Student Course API is running"
}
```

### 4.2 Get all courses

| | |
| --- | --- |
| Method | `GET` |
| URL | `/api/courses` |
| Success | `200 OK` |

Returns a JSON **array** with five course objects. Each object contains an integer `id`, plus `code`, `name`, and `description`.

```json
[
  {
    "id": 1,
    "code": "ITAS 3228",
    "name": "Web and Mobile Development",
    "description": "Build responsive websites and mobile-ready interfaces using modern front-end tools and API-driven development."
  },
  {
    "id": 2,
    "code": "ITAS 3218",
    "name": "Database Management",
    "description": "Design relational schemas, write SQL queries, and keep data accurate through constraints and transactions."
  }
]
```

### 4.3 Get course by ID

| | |
| --- | --- |
| Method | `GET` |
| URL | `/api/courses/<id>` |
| Success | `200 OK` — the matching course |
| Not found | `404 Not Found` — JSON error message |

Success example (`/api/courses/3`):

```json
{
  "id": 3,
  "code": "ITAS 3208",
  "name": "System Integration and Architecture",
  "description": "Connect separate systems through APIs and integration patterns so enterprise workflows run end to end."
}
```

Not-found example (`/api/courses/9999`):

```json
{
  "status": "error",
  "message": "Course with id 9999 was not found"
}
```

---

## 5. Installation

Requirements: **Python 3.9 or newer** (`python --version` to check).

```bash
# 1. Go into the project folder
cd student_course_api

# 2. Create a virtual environment
python -m venv venv

# 3. Activate it
# Windows (Command Prompt):
venv\Scripts\activate
# Windows (PowerShell):
venv\Scripts\Activate.ps1
# macOS / Linux:
source venv/bin/activate

# 4. Install the dependencies
pip install -r requirements.txt
```

---

## 6. Run the backend locally

```bash
python app.py
```

The terminal prints something like:

```
Running on http://0.0.0.0:5000
```

Reads `PORT` from the environment, defaults to `5000`, and binds to `0.0.0.0`.

To use a different port:

```bash
# Windows PowerShell
$env:PORT=8080; python app.py
# macOS / Linux
PORT=8080 python app.py
```

You can also run it the production way (same command Render uses):

```bash
gunicorn app:app
```

---

## 7. Testing the API

### Option A — browser

Open these URLs while the server is running:

- <http://127.0.0.1:5000/api/health>
- <http://127.0.0.1:5000/api/courses>
- <http://127.0.0.1:5000/api/courses/1>
- <http://127.0.0.1:5000/api/courses/9999> ← should show the JSON error

### Option B — curl (shows the status code)

```bash
curl -i http://127.0.0.1:5000/api/health
curl -i http://127.0.0.1:5000/api/courses
curl -i http://127.0.0.1:5000/api/courses/1
curl -i http://127.0.0.1:5000/api/courses/9999
```

The first line of each response shows the status:

```
HTTP/1.1 200 OK
HTTP/1.1 200 OK
HTTP/1.1 200 OK
HTTP/1.1 404 NOT FOUND
```

### Option C — Postman

Create a request, choose **GET**, paste the URL, press **Send**, and read the status code and JSON body.

---

## 8. Upload to GitHub

### Option A — Git commands

```bash
cd student_course_api
git init
git add .
git commit -m "Student Course API - Flask backend"
git branch -M main
git remote add origin https://github.com/USERNAME/student-course-api.git
git push -u origin main
```

Create the empty repository on GitHub first (no README, no .gitignore) so the push has somewhere to go.

### Option B — GitHub website

1. Create a new repository.
2. Click **uploading an existing file**.
3. Drag in `app.py`, `requirements.txt`, `README.md`, and `.gitignore`.
4. Commit the changes.

---

## 9. Deploy to Render

1. Sign in at <https://render.com> with GitHub.
2. Click **New +** → **Web Service**.
3. Choose **Build and deploy from a Git repository**, then connect the repository you just pushed.
4. Fill in the settings:

| Setting | Value |
| --- | --- |
| Name | `student-course-api` (or any name) |
| Language / Runtime | `Python 3` |
| Branch | `main` |
| Root Directory | leave blank (if the repo root **is** the project folder) |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| Instance Type | Free |

> If you uploaded the files inside a subfolder, set **Root Directory** to that folder name.

5. Choose the **Free** instance type and click **Create Web Service**.
6. Wait for the log to show `Booting worker with pid ...` and `Your service is live 🎉`.

Render assigns the `PORT` environment variable automatically — `app.py` already reads it, and Gunicorn binds to `0.0.0.0`.

---

## 10. Verify the deployment

Replace `YOUR-RENDER-URL` with your real service URL (for example `https://student-course-api.onrender.com`).

| URL | Expected |
| --- | --- |
| `https://YOUR-RENDER-URL.onrender.com/api/health` | `200` + success message |
| `https://YOUR-RENDER-URL.onrender.com/api/courses` | `200` + array of 5 courses |
| `https://YOUR-RENDER-URL.onrender.com/api/courses/1` | `200` + course id 1 |
| `https://YOUR-RENDER-URL.onrender.com/api/courses/9999` | `404` + JSON error |

> The free Render instance sleeps after about 15 minutes of inactivity. The first request after that can take 30–60 seconds while it wakes up.

---

## 11. Limitations and notes

- **Read-only:** only `GET` routes exist. Any other method returns `405` with a JSON message.
- **No database:** the five courses live in a Python list. Restarting the service restores the original data, because nothing is ever changed.
- **No authentication:** the API is intentionally open for a classroom demonstration. Do not store personal data in it.
- **Separate from any frontend:** this is a standalone backend. It does not depend on another application to run.
