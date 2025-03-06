import streamlit as st
import pandas as pd
import requests  # Para enviar arquivos para o n8n

st.title("Anotações Multimídia")

# Abas do aplicativo
abas = st.tabs(["Envio de Arquivos", "Visão de Nós", "Anotações"])

# Aba 1: Envio de Arquivos
with abas[0]:
    st.header("Envio de Arquivos")
    arquivo = st.file_uploader("Selecione um arquivo", type=["png", "jpg", "jpeg", "mp3", "mp4", "wav", "pdf", "txt", "docx"])
    if arquivo:
        if st.button("Enviar para Análise"):
            # Enviar arquivo para o n8n
            enviar_arquivo_n8n(arquivo)
            st.success("Arquivo enviado para análise!")

# Aba 2: Visão de Nós
with abas[1]:
    st.header("Visão de Nós")
    # Lógica para construir a visão de nós (a ser implementada)

# Aba 3: Anotações
with abas[2]:
    st.header("Anotações")
    # Lógica para exibir as anotações (a ser implementada)

# Função para enviar arquivo para o n8n
def enviar_arquivo_n8n(arquivo):
    # Configurar a URL do webhook do n8n
    webhook_url = "YOUR_N8N_WEBHOOK_URL"  # Substitua pela sua URL do webhook

    # Enviar arquivo para o n8n
    files = {"arquivo": arquivo}
    response = requests.post(webhook_url, files=files)

    # Verificar a resposta do n8n
    if response.status_code == 200:
        print("Arquivo enviado com sucesso para o n8n!")
    else:
        print(f"Erro ao enviar arquivo para o n8n: {response.status_code}")