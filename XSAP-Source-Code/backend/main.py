from fastapi import FastAPI

app = FastAPI(
    title="Xeonsys Stock Analytics Platform API",
    description="Backend API for XSAP",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "success",
        "message": "XSAP API is running"
    }