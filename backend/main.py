from fastapi import FastAPI
app= FastAPI(
    title="GitPulse API",
    description="API for GitPulse, a tool to analyze GitHub repositories and provide insights.",
    version="1.0.0",
)
@app.get("/")
def read_root():
    return {"message": "Welcome to the GitPulse"}