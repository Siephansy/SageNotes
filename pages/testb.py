import streamlit as st
import requests

# Configurar a URL do webhook do n8n - DEIXE CONFIGURÁVEL NO CÓDIGO
webhook_url = "http://127.0.0.1:5678/webhook-test/7109995a-fbfa-4b8a-8049-8ee62622d853"  # COLOQUE A SUA URL DO N8N AQUI


def run_connection_test():
    """Executa o teste de conexão ao webhook e exibe o resultado no Streamlit."""
    try:
        response = requests.post(webhook_url)
        if response.status_code == 200:
            st.success("Teste de conexão bem-sucedido!")
            st.write("Resposta do servidor:")
            st.code(response.text, language="json") # Exibe a resposta formatada como JSON
        else:
            st.error(f"Erro no teste de conexão. Código de estado: {response.status_code}")
            st.write("Resposta de erro do servidor:")
            st.code(response.text, language="json") # Exibe a resposta de erro formatada como JSON
    except requests.ConnectionError as e:
        st.error(f"Erro de conexão: {e}")


st.title("Teste de Conexão Webhook n8n")
st.markdown("Clique no botão abaixo para testar a conexão com o webhook do n8n.")

if st.button("Testar Conexão"):
    run_connection_test()