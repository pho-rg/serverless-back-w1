from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from azure.storage.blob import BlobServiceClient
import os
import json
from dotenv import load_dotenv

# Configuration Azure Blob Storage
AZURE_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=storagebros;AccountKey=Ix9SHXlpJjuAGz2QnDWupLtUl1C9kcqH79XYE8daleIrMrS2hKecI/hoHaFr0nSTQGTtHxF6Tbhk+AStGrAT9A==;EndpointSuffix=core.windows.net"
CONTAINER_CSV = "csv-uploads"
CONTAINER_JSON = "json-report"

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
