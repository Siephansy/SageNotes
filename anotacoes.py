import streamlit as st
import pandas as pd

def exibir_anotacoes():
    st.header("Anotações")
    # Lógica para exibir as anotações
    # (Leia os dados do Google Sheets e exiba em uma tabela ou lista)
    # Exemplo simples (substitua pela sua lógica real):
    data = {"Título": ["Anotação 1", "Anotação 2"], "Data": ["2023-10-26", "2023-10-27"]}
    df = pd.DataFrame(data)
    st.dataframe(df)