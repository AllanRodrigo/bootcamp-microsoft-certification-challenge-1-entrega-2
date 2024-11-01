import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENDPOINT = os.getenv("DOC_ENDPOINT")
    KEY = os.getenv("DOC_KEY")
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("STORAGE_CONNECTION_STRING")
    STORAGE_NAME = os.getenv("STORAGE_NAME")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")