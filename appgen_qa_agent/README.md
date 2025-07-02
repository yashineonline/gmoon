# appgen_qa_agent/README.md

# 🔍 AppGen QA Agent

> An LLM-powered code QA tool for mobile apps (iOS/Android) — detects policy violations, accessibility issues, and security flaws before submission.

---

## 🎯 Why?

As AI-generated apps flood the stores, **first-pass QA** becomes essential. This agent automates store-readiness checks:

- App Store & Play Store rejection criteria
- Accessibility & UX flaws
- Code quality and anti-patterns
- Dangerous permissions & APIs

---

## 🛠️ Built With

- Python 3.11
- FastAPI
- GPT-4o (via OpenAI API or local model)
- Store policy datasets (Apple & Google)

---

## 🚀 How It Works

1. Upload `.zip` file or paste code snippet
2. Agent scans for known issues
3. Returns markdown report with ✅, ⚠️, 🚩 flags

---

## 💻 Example Output

```markdown
🚩 Missing `NSCameraUsageDescription` — causes iOS rejection  
✅ Good use of safe area on iOS  
⚠️ `WRITE_EXTERNAL_STORAGE` used without UI toggle — Android may flag
```

---

## 🔌 API Usage (FastAPI)

```http
POST /analyze_code
Body: { "code": "..." } OR { "zip_file": binary }
Response: QA markdown report
```

---

## 🧪 Try It (Demo Mode)

```bash
git clone https://github.com/your-username/AppGen-QA-Agent.git
cd AppGen-QA-Agent
pip install -r requirements.txt
uvicorn main:app --reload
```
Open: `http://localhost:8000/docs`

---

## 📚 Policy Datasets Used
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Google Play Policies](https://support.google.com/googleplay/android-developer/answer/9857753)

---

## 📌 Roadmap
- ✅ Markdown report scoring
- 🔄 Upload `.zip` support
- 🔐 API key auth for large batch jobs
- 🌐 Web UI (Streamlit or Next.js frontend)

---

## 🙌 Contribute
Want to add more policy checks or expand to web apps? PRs are welcome.

---

## 👤 Author
Yashine Hazmatally Goolam Hossen – Waterloo, Canada

## Endorsement

Paragon Research Labs
