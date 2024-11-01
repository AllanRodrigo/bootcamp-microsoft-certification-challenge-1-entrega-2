import streamlit as st
from utils.config import Config
from azure.storage.blob import BlobServiceClient

def uploadBlob(arq, nome_arq):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=nome_arq)
        blob_client.upload_blob(arq, overwrite=True)
        return blob_client.url
    except Exception as ex:
        st.error(f"Erro ao enviar o arquivo: {ex}!")        
        return None