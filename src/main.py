from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from controller import TranslatorController
from dtypes import make_response


app = FastAPI(
    title="Major Project Translation Service",
    description="Translation Service for Major Project",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/api/v1/translate/openapi.json",
    contact={
        "name": "Abhiram B.S.N.",
        "email": "abhirambsn@gmail.com",
        "url": "https://abhirambsn.com"
    }
)

app.include_router(TranslatorController)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def perform_health_check(response: Response):
    return make_response(response, status=200, message="Healthy", data=None)