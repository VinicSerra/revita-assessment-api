from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app import modules


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(modules.assessment.router)
app.include_router(modules.auth.router)
app.include_router(modules.patient.router)



if __name__ == "__main__":
    uvicorn.run(app, host=str("0.0.0.0"), port=int(8000))

