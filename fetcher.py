import requests
from datetime import datetime, timedelta

def parse_codechef_datetime(s):
    s = " ".join(s.split())
    for fmt in ("%Y-%m-%d %H:%M:%S", "%d %b %Y %H:%M:%S"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    raise ValueError(f"Unknown CodeChef date format: {s}")


def fetch_codeforces():
    url = "https://codeforces.com/api/contest.list"
    data = requests.get(url).json()
    now = datetime.now()

    contests = []
    for c in data["result"]:
        start = datetime.fromtimestamp(c["startTimeSeconds"])
        end = start + timedelta(seconds=c["durationSeconds"])

        if c["phase"] == "BEFORE":
            contest_url = "https://codeforces.com/contests"
        else:
            contest_url = f"https://codeforces.com/contest/{c['id']}"

        contests.append({
            "platform": "Codeforces",
            "name": c["name"],
            "start_time": start,
            "end_time": end,
            "duration_min": c["durationSeconds"] // 60,
            "url": contest_url
        })
    return contests


def fetch_codechef():
    url = "https://www.codechef.com/api/list/contests/all"
    headers = {"User-Agent": "Mozilla/5.0"}
    now = datetime.now()

    r = requests.get(url, headers=headers, timeout=10)
    if r.status_code != 200:
        return []

    try:
        data = r.json()
    except Exception:
        return []

    contests = []

    for c in data.get("present_contests", []) + data.get("future_contests", []):
        start = parse_codechef_datetime(c["contest_start_date"])
        duration = int(c["contest_duration"])
        end = start + timedelta(minutes=duration)

        if start > now:
            contest_url = "https://www.codechef.com/contests"
        else:
            contest_url = f"https://www.codechef.com/{c['contest_code']}"

        contests.append({
            "platform": "CodeChef",
            "name": c["contest_name"],
            "start_time": start,
            "end_time": end,
            "duration_min": duration,
            "url": contest_url
        })

    return contests


def fetch_atcoder():
    url = "https://kenkoooo.com/atcoder/resources/contests.json"
    data = requests.get(url).json()
    now = datetime.now().timestamp()

    contests = []
    for c in data:
        start = datetime.fromtimestamp(c["start_epoch_second"])
        end = start + timedelta(seconds=c["duration_second"])

        if c["start_epoch_second"] > now:
            contest_url = "https://atcoder.jp/contests/"
        else:
            contest_url = f"https://atcoder.jp/contests/{c['id']}"

        contests.append({
            "platform": "AtCoder",
            "name": c["title"],
            "start_time": start,
            "end_time": end,
            "duration_min": c["duration_second"] // 60,
            "url": contest_url
        })

    return contests
