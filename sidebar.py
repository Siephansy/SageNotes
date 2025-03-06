import streamlit as st

def sidebar_content():
    st.sidebar.header("Navegação")
    pagina_selecionada = st.sidebar.radio("Selecione uma página", ["Envio de Arquivos", "Visão de Nós", "Anotações"])
    return pagina_selecionada