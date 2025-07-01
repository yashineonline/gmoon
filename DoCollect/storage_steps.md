# DoCollect/storage_steps.md

## ✅ Step 1: Choose Storage – Google Drive vs Firebase

| Feature          | Firebase Storage               | Google Drive API               |
|------------------|--------------------------------|--------------------------------|
| 🔐 Auth          | Fine-grained user control (OAuth, tokens) | OAuth needed, limited scopes |
| 💾 Free quota    | ~5GB for Cloud Storage         | 15GB shared across Google services |
| ⚙️ Complexity   | Moderate (Firebase CLI & SDK)  | Higher setup, especially for upload/write |
| 🧩 Streamlit usage | Common via pyrebase          | Tricky due to OAuth flows |

---

### ✅ Recommendation: 
Use **Firebase Cloud Storage with pyrebase** for:
- Better Streamlit integration
- Programmatic control
- Easier expansion later (user auth, tagging, etc.)

---

## ✅ Step 2: Update the DocCollect MVP to Upload to Firebase

You'll need:
1. A free [Firebase account](https://console.firebase.google.com)
2. Create a new project
3. Enable Cloud Storage
4. Get the Firebase config (Project Settings → Web App)
5. Create a Firebase service account and get the `firebaseConfig`

---

## ✅ Step 3: Install Required Packages

Update your `requirements.txt`:
```text
streamlit
pyrebase4
```

---

## ✅ Step 4: Update app.py with Firebase Upload

Code will:
- Upload user files to your Firebase bucket
- Save links in `submissions.json`

---

## ✅ Step 5: Get Public Link to Share

After deploying on [Streamlit Cloud](https://share.streamlit.io):
1. Connect your GitHub repo
2. Streamlit will generate a public link like:
   ```text
   https://your-username-doccollect.streamlit.app
   ```
3. Paste this in your QR or community messages
