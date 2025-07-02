### appgen_qa_agent/qa_rules.py
import zipfile
import io
from appgen_qa_agent.policy_data.ios_rules import ios_rules
from appgen_qa_agent.policy_data.android_rules import android_rules

def analyze_code_snippet(code: str) -> str:
    report = []
    for rule in ios_rules + android_rules:
        if rule["trigger"] in code:
            report.append(f"{rule['flag']} {rule['description']}")
    return "\n".join(report) or "✅ No critical issues detected."

async def analyze_zip_file(file) -> str:
    contents = await file.read()
    zip_data = zipfile.ZipFile(io.BytesIO(contents))
    all_code = ""
    for name in zip_data.namelist():
        if name.endswith(('.swift', '.kt', '.java', '.xml', '.plist')):
            with zip_data.open(name) as f:
                all_code += f.read().decode("utf-8", errors="ignore") + "\n"
    return analyze_code_snippet(all_code)


