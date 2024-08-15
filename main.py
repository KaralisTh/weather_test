from fastapi import FastAPI
from Controllers import weatherController
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

port = int(os.getenv('PORT', 8000))

@app.get("/")
async def read_root():
    print("Root endpoint accessed")
    return {"message": "Welcome to the weather API!"}

app.include_router(weatherController.router, prefix="/api/weather")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
