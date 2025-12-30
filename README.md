# 🖥️ Contests & Hackathons Tracker

A *web application* that shows **upcoming** and **ongoing programming contests** from popular platforms like **Codeforces**, **CodeChef**, and **AtCoder**. Quickly see which contests are happening, their start times, durations, and direct links to participate.

The project is **hosted on Render**, so you can view it: [Website](https://cpcontests.onrender.com)

---

## Features

- **Upcoming Contests** – See contests that will start in the future.  
- **Ongoing Contests** – Keep track of contests currently running.  
- **Platform Filters** – Filter contests by **Codeforces**, **CodeChef**, or **AtCoder**.  
- **Contest Details** – Name, start time, duration, and a link to the contest.  
- **Responsive Design** – Works on both desktop and mobile devices.  
- **Live Updates** – Fetches contest data directly from official APIs and public endpoints.

---

## How It Works

The backend fetches contests from:  

1. **Codeforces API** – [https://codeforces.com/apiHelp](https://codeforces.com/apiHelp)  
2. **CodeChef API** – [https://www.codechef.com/api/list/contests/all](https://www.codechef.com/api/list/contests/all)  
3. **AtCoder JSON Endpoint** – (Ongoing...)

The **FastAPI backend** provides a `/contests` endpoint that serves the contest data.  
The **frontend** fetches this data and displays it with **filters**, **sections for ongoing/upcoming contests**, and a **clean, responsive layout**.

---

## Live Website

Check out the live website here:  

[https://cpcontests.onrender.com](https://cpcontests.onrender.com)

---

## Running Locally

### Prerequisites

- Python 3.10+  
- `pip` package manager  

---

### Linux / macOS

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/ContestsTimings.git
cd ContestsTimings

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the FastAPI server
uvicorn api:app --reload

# 5. Open the frontend
# Navigate to http://127.0.0.1:8000 in your browser
```
### Windows

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/ContestsTimings.git
cd ContestsTimings

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the FastAPI server
uvicorn api:app --reload

# 5. Open the frontend
# Navigate to http://127.0.0.1:8000 in your browser
```

### Project Structure

```bash
ContestsTimings/
│
├─ api.py           # FastAPI backend serving /contests API
├─ fetcher.py       # Functions to fetch contests from Codeforces, CodeChef, AtCoder
├─ frontend/        # Frontend files
│   └─ index.html
├─ requirements.txt # Python dependencies
└─ README.md        # This file
```

### Dependencies

1. [FastAPI](https://fastapi.tiangolo.com/) - backend framework
2. [Uvicorn](https://www.uvicorn.org/) - ASGI Server
3. [Requests](https://requests.readthedocs.io/en/latest/) - HTTP requests to fetch contest data

Install dependencies with:
```bash
pip install -r requirements.txt
```

### Notes
1. Hosted on Render. Free plan has a ~15 minute idle timeout if not accessed.
2. Designed for educational and personal use to track programming contests efficiently.
