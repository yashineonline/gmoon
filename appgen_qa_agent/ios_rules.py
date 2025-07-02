### appgen_qa_agent/policy_data/ios_rules.py
ios_rules = [
    {"trigger": "NSCameraUsageDescription", "flag": "🚩", "description": "Missing `NSCameraUsageDescription` — causes iOS rejection"},
    {"trigger": "UIWebView", "flag": "⚠️", "description": "Deprecated `UIWebView` used — Apple may reject"},
    {"trigger": "!safeAreaLayoutGuide", "flag": "⚠️", "description": "Unsafe layout detected — check safe area constraints"},
]
