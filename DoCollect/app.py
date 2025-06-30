import streamlit as st
import os
import json
from datetime import datetime

UPLOAD_DIR = "uploads"
DATA_PATH = "data/submissions.json"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs("data", exist_ok=True)

st.title("📤 Community Documentation Submission Portal")

text = st.text_area("Write something you'd like to share (optional)")
url = st.text_input("Or paste a link (e.g., Google Drive, Dropbox, YouTube)")
files = st.file_uploader("Upload any files (pdf, mp4, txt, mp3, etc.)", accept_multiple_files=True)

if st.button("Submit"):
    timestamp = datetime.utcnow().isoformat()
    submission = {
        "text": text,
        "url": url,
        "files": [],
        "time": timestamp
    }

    for uploaded_file in files:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        submission["files"].append(uploaded_file.name)

    if os.path.exists(DATA_PATH):
        with open(DATA_PATH) as f:
            data = json.load(f)
    else:
        data = []

    data.append(submission)
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)

    st.success("✅ Submission received! Thank you.")
