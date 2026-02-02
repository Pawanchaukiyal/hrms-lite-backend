# Entry point of backend app
# Creates FastAPI instance and root test route

from fastapi import FastAPI

app = FastAPI(title="HRMS Lite API")

@app.get("/")
def root():
    return {"message": "HRMS Lite backend running"}
