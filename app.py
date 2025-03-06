import streamlit as st
import requests
import sidebar  # Importa a lógica da barra lateral

st.title("Anotações Multimídia")

# Barra lateral
pagina_selecionada = sidebar.sidebar_content()

# Conteúdo principal (envio de arquivos)
if pagina_selecionada == "Envio de Arquivos":
    st.header("Envio de Arquivos")
    arquivo = st.file_uploader("Selecione um arquivo", type=["png", "jpg", "jpeg", "mp3", "mp4", "wav", "pdf", "txt", "docx"])
    if arquivo:
        if st.button("Enviar para Análise"):
            # Enviar arquivo para o n8n
            enviar_arquivo_n8n(arquivo)
            st.success("Arquivo enviado para análise!")

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