import streamlit as st
import webbrowser
import pandas as pd
import requests
from datetime import datetime

# Configurar a URL do webhook do n8n
webhook_url = "http://127.0.0.1:5678/webhook/7109995a-fbfa-4b8a-8049-8ee62622d853"  # Substitua pela sua URL do webhook


# Função para enviar um teste simples para o webhook do n8n
def testar_webhook_n8n():
    try:
        response = requests.post(webhook_url)  # Envia um POST simples, sem arquivo
        if response.status_code == 200:
            st.success("Teste de conexão ao webhook bem-sucedido! (Código 200 OK)")
            print("Teste de conexão ao webhook bem-sucedido! (Código 200 OK)")
        else:
            st.error(f"Erro no teste de conexão ao webhook. Código de estado: {response.status_code}")
            print(f"Erro no teste de conexão ao webhook. Código de estado: {response.status_code}")
            print("Resposta do servidor:")
            print(response.text)  # Imprime detalhes da resposta de erro do n8n
    except requests.ConnectionError as e:
        st.error(f"Erro de conexão ao webhook: {e}")
        print(f"Erro de conexão ao webhook: {e}")


# Função para enviar arquivo para o n8n
def enviar_arquivo_n8n(arquivo):
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
            print(response.text)  # Imprime detalhes da resposta de erro do n8n
    except Exception as e:
        st.error(f"Erro ao enviar o arquivo: {e}")
        print(f"Erro ao enviar o arquivo: {e}")


st.set_page_config(page_title="Anotações Multimídia", layout="centered")
st.markdown("Anotações Multimídia")

st.header("Testar Conexão Webhook")  # Nova secção para o botão de teste
if st.button("Testar Conexão Webhook"):
    testar_webhook_n8n()  # Chama a função de teste ao clicar no botão

st.header("Envio de Arquivos") # Secção de envio de arquivos (mantém-se como estava)
arquivo = st.file_uploader("Selecione um arquivo", type=["png", "jpg", "jpeg", "mp3", "mp4", "wav", "pdf", "txt", "docx"])
if arquivo:
    if st.button("Enviar para Análise"):
        # Enviar arquivo para o n8n
        enviar_arquivo_n8n(arquivo) # Chamada CORRIGIDA da função enviar_arquivo_n8n, passando 'arquivo' como argumento