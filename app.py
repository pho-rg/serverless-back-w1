from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from azure.storage.blob import BlobServiceClient
import os
import json
from dotenv import load_dotenv

# Initialiser l'application FastAPI
app = FastAPI()

# Activer CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# root
@app.get("/")
def read_root():
    return "CSVitesse"
