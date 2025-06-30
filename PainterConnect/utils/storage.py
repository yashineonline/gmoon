import json
import os

DATA_PATH = "data/jobs.json"

def load_jobs():
    if not os.path.exists(DATA_PATH):
        return []
    with open(DATA_PATH, 'r') as f:
        return json.load(f)

def save_job(job):
    jobs = load_jobs()
    jobs.append(job)
    with open(DATA_PATH, 'w') as f:
        json.dump(jobs, f, indent=2)
