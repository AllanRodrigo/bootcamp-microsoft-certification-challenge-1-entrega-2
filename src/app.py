import streamlit as st
from services.blob_service import uploadBlob

from services.credit_card_service import analisarDocumentos

def criar_tela():
    st.title("Upload de arquivos DIO - Desafio 2 - Azure Ai Fundamentals")
    arq_up = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])
    
    if arq_up is not None:
        nome_arq = arq_up.name
        
        blob_url = uploadBlob(arq_up, nome_arq)
        if blob_url:
            st.write(f"Arquivo {nome_arq} enviado com sucesso!")
            cartao_info = analisarDocumentos(blob_url)
            
            exibir_img_validacao(blob_url, cartao_info)
        else:
            st.write(f"Erro ao enviar o arquivo {nome_arq}!")
            
def exibir_img_validacao(blob_url, cartao_info):
    st.image(blob_url, caption="Imagem enviada")
    st.write("Resultado da validação:")
    
    if cartao_info and cartao_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Cartão válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {cartao_info["card_name"]}")
        st.write(f"Banco Emissor: {cartao_info["bank_name"]}")
        st.write(f"Data de validade: {cartao_info["expiry_date"]}")
        st.write(f"Bandeira: {cartao_info["flag"]}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão inválido</h1>", unsafe_allow_html=True)
        st.write("Este não é um cartão de crédito válido.")

if __name__ == "__main__":
    criar_tela()  