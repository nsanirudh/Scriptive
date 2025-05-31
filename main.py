import nltk

nltk.download("punkt", quiet=True)
nltk.download('punkt_tab')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modules.api.routes import router

app = FastAPI(title="Scriptive API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
