import streamlit as st
import webbrowser
import pandas as pd
import requests
from datetime import datetime 


# Função para enviar arquivo para o n8n
def enviar_arquivo_n8n(arquivo):
    # Configurar a URL do webhook do n8n
    webhook_url = "http://127.0.0.1:5678/webhook/7109995a-fbfa-4b8a-8049-8ee62622d853"  # Substitua pela sua URL do webhook

    # Enviar arquivo para o n8n
    try:
        files = {"arquivo": (arquivo.name, arquivo, arquivo.type)}  # Formato correto para enviar arquivos com requests
        response = requests.post(webhook_url, files=files)

        # Verificar a resposta do n8n
        if response.status_code == 200:
            st.success("Arquivo enviado com sucesso para o n8n!")
            print("Arquivo enviado com sucesso para o n8n!")
        else:
            st.error(f"Erro ao enviar arquivo para o n8n: {response.status_code}")
            print(f"Erro ao enviar arquivo para o n8n: {response.status_code}")
            print(response.text) # Print the error returned by n8n
    except Exception as e:
        st.error(f"Erro ao enviar o arquivo: {e}")
        print(f"Erro ao enviar o arquivo: {e}")



st.set_page_config(page_title="Anotações Multimídia", layout="centered")
st.markdown("Anotações Multimídia")

st.header("Envio de Arquivos")
arquivo = st.file_uploader("Selecione um arquivo", type=["png", "jpg", "jpeg", "mp3", "mp4", "wav", "pdf", "txt", "docx"])
if arquivo:
    if st.button("Enviar para Análise"):
        # Enviar arquivo para o n8n
        enviar_arquivo_n8n(arquivo)
