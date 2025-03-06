import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def sidebar_content():
    st.sidebar.header("Navegação")
    opcao = st.sidebar.radio("Selecione uma opção", ["Visão de Nós", "Anotações"])

    if opcao == "Visão de Nós":
        st.sidebar.subheader("Visão de Nós")
        exibir_visao_nos()
    elif opcao == "Anotações":
        st.sidebar.subheader("Anotações")
        exibir_anotacoes()

def exibir_visao_nos():
    # Lógica para construir e exibir a visão de nós
    # (Leia os dados do Google Sheets e use networkx)
    # Exemplo simples (substitua pela sua lógica real):
    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    st.sidebar.pyplot(plt)

def exibir_anotacoes():
    # Lógica para exibir as anotações
    # (Leia os dados do Google Sheets e exiba em uma tabela ou lista)
    # Exemplo simples (substitua pela sua lógica real):
    data = {"Título": ["Anotação 1", "Anotação 2"], "Data": ["2023-10-26", "2023-10-27"]}
    df = pd.DataFrame(data)
    st.sidebar.dataframe(df)