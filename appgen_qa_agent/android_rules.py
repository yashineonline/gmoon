### appgen_qa_agent/policy_data/android_rules.py
android_rules = [
    {"trigger": "WRITE_EXTERNAL_STORAGE", "flag": "⚠️", "description": "`WRITE_EXTERNAL_STORAGE` used without UI toggle — Android may flag"},
    {"trigger": "REQUEST_INSTALL_PACKAGES", "flag": "🚩", "description": "`REQUEST_INSTALL_PACKAGES` requires policy declaration — common rejection reason"},
    {"trigger": "android.permission.READ_SMS", "flag": "🚩", "description": "Sensitive permission `READ_SMS` — must justify usage"},
]
