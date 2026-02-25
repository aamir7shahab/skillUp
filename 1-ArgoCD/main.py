from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0", "message": "GitOps multi-arch deployment successful"}
