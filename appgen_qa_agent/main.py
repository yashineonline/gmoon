### appgen_qa_agent/main.py
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from appgen_qa_agent.qa_rules import analyze_code_snippet, analyze_zip_file

app = FastAPI()

@app.post("/analyze_code")
async def analyze_code(code: str = Form(None), file: UploadFile = File(None)):
    if code:
        result = analyze_code_snippet(code)
        return JSONResponse(content={"report": result})
    elif file:
        result = await analyze_zip_file(file)
        return JSONResponse(content={"report": result})
    else:
        return JSONResponse(status_code=400, content={"error": "No input provided"})


