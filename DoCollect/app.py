import streamlit as st
import os
import json
from datetime import datetime, timezone

# Allowed file types
ALLOWED_FILE_TYPES = ["pdf", "mp4", "txt", "mp3", "png", "jpg", "jpeg"]


UPLOAD_DIR = "uploads"
DATA_PATH = "data/submissions.json"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs("data", exist_ok=True)

st.title("📤 Community Documentation Submission Portal")

# Mandatory subject section with dropdown
subject_options = ["Tutorial", "Research", "Case Study", "Other"]
subject = st.selectbox("Subject (mandatory)", options=subject_options, index=None, placeholder="Select a subject")


# Show additional text box if "Other" is selected
other_subject = ""
if subject == "Other":
    other_subject = st.text_input("Please specify the subject")

# Ensure subject is filled
if subject is None:
    st.error("Please select a subject.")
    st.stop()

title = st.text_area("Title (optional)")
text = st.text_area("Write something you'd like to share (optional)")
url = st.text_input("Or paste a link (e.g., Google Drive, Dropbox, YouTube)")
files = st.file_uploader("Upload any files (pdf, mp4, txt, mp3, etc.)", accept_multiple_files=True)

if st.button("Submit"):
     # Validate file types
    for uploaded_file in files:
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension not in ALLOWED_FILE_TYPES:
            st.error(f"File type '{file_extension}' is not allowed.")
            st.stop()

    timestamp = datetime.now(timezone.utc).isoformat()
    submission = {
        "subject": subject if subject != "Other" else other_subject,
        "title": text,
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
