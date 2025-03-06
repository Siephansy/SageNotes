import streamlit as st
import time
import random
import networkx as nx
import matplotlib.pyplot as plt




st.header("Visão de Nós")
# Lógica para construir e exibir a visão de nós
# (Leia os dados do Google Sheets e use networkx)
# Exemplo simples (substitua pela sua lógica real):
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
st.pyplot(plt)



st.header("Anotações")
# Lógica para exibir as anotações
# (Leia os dados do Google Sheets e exiba em uma tabela ou lista)
# Exemplo simples (substitua pela sua lógica real):
#data = {"Título": ["Anotação 1", "Anotação 2"], "Data": ["2023-10-26", "2023-10-27"]}
#df = pd.DataFrame(data)
#st.dataframe(df)

