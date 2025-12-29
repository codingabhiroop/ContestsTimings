from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from datetime import datetime

from fetcher import fetch_codeforces, fetch_codechef, fetch_atcoder

app = FastAPI(title="Contests & Hackathons API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/contests")
def get_contests():
    now = datetime.now()

    contests = []
    contests += fetch_codeforces()
    contests += fetch_codechef()
    contests += fetch_atcoder()

    result = []

    for c in contests:
        if c["start_time"] <= now <= c["end_time"]:
            status = "ONGOING"
        elif c["start_time"] > now:
            status = "UPCOMING"
        else:
            continue

        result.append({
            "platform": c["platform"],
            "name": c["name"],
            "start_time": c["start_time"].isoformat(),
            "end_time": c["end_time"].isoformat(),
            "duration_min": c["duration_min"],
            "url": c["url"],
            "status": status
        })

    result.sort(key=lambda x: x["start_time"])
    return result


app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
