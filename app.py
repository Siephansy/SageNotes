import streamlit as st
import webbrowser
import pandas as pd
import requests
from datetime import datetime 

st.set_page_config(page_title="Anotações Multimídia", layout="centered")
st.markdown("Anotações Multimídia")

st.header("Envio de Arquivos")
arquivo = st.file_uploader("Selecione um arquivo", type=["png", "jpg", "jpeg", "mp3", "mp4", "wav", "pdf", "txt", "docx"])
if arquivo:
    if st.button("Enviar para Análise"):
        # Enviar arquivo para o n8n
        enviar_arquivo_n8n(arquivo)
        st.success("Arquivo enviado para análise!")