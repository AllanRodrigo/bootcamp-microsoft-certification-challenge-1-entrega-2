from utils.config import Config
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

def analisarDocumentos(card_url):
    credential = AzureKeyCredential(Config.KEY)
    doc_int_client = DocumentIntelligenceClient(Config.ENDPOINT, credential)
    
    docInfo = doc_int_client.begin_analyze_document("prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url))
    result = docInfo.result()
    
    for doc in result.documents:
        item = doc.get('fields', {})
        
        return {
            "card_name": item.get('CardHolderName', {}).get('content'),
            "card_number": item.get('CardNumber', {}).get('content'),
            "expiry_date": item.get('ExpirationDate', {}).get('content'),
            "bank_name": item.get('IssuingBank', {}).get('content'),
            "flag": item.get('PaymentNetwork', {}).get('content'),
        }