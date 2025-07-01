# Painter MVP

## 🚀 Mobile-Ready Version (Frontend)
- use Next.js + Tailwind CSS for the frontend and Supabase or Firebase as backend.

- Generate a basic mobile-first responsive UI with job listing + painter profile input

- Add backend stubs (API routes or Firebase rules)

- Keep Streamlit as a fallback lightweight desktop interface

### To choose frontend stack:

✅ Next.js + Tailwind (best for mobile+web)

🔁 Flutter (best for native apps)

⬇️ React Native (also solid but a bit heavier)

🟠 Keep Streamlit (for MVP simplicity)


### Streamlit works on mobile, but with limitations:

#### 📱 Streamlit on Mobile: What Works

✅ Loads in mobile browsers (Safari, Chrome, etc.)

✅ Input forms, buttons, sliders, and outputs scale reasonably

✅ Good for demo, pilot tests, and investor pitches

#### ⚠️ Limitations

❌ No native push notifications

❌ Not mobile app-store installable (no APK/IPA)

❌ Limited styling/customization (without hacks or plugins)

❌ No offline mode or native mobile APIs

### ✅ Current Plan

Now: MVP via Streamlit — rapid, no infra stress

Later: Rebuild into:

Next.js + Tailwind + Supabase for mobile web

Optionally wrap it into PWA or native apps via Capacitor/Expo

