import streamlit as st
import time
import random
import networkx as nx
import matplotlib.pyplot as plt

# Dados do quiz
quiz_data = [
    {
        "pergunta": "Qual é a capital da França?",
        "opcoes": ["Berlim", "Madri", "Paris", "Lisboa"],
        "resposta_correta": "Paris"
    },
    {
        "pergunta": "Quem escreveu 'Dom Quixote'?",
        "opcoes": ["Miguel de Cervantes", "Gabriel Garcia Marquez", "William Shakespeare", "Victor Hugo"],
        "resposta_correta": "Miguel de Cervantes"
    },
    {
        "pergunta": "Qual é o maior planeta do sistema solar?",
        "opcoes": ["Terra", "Marte", "Júpiter", "Saturno"],
        "resposta_correta": "Júpiter"
    }
]


# Inicialização do estado
if "initialized" not in st.session_state:
    # Configuração inicial de pontuação
    st.session_state.pontuacao = 0

    # Embaralha as opções para cada pergunta
    for questao in quiz_data:
        random.shuffle(questao["opcoes"])

    # Marca como inicializado
    st.session_state.initialized = True

# Função para mostrar o placar que pisca em RGB
def show_score(score, is_correct):
    # Se a resposta foi correta, mostramos o placar com animação RGB
    if is_correct:
        st.markdown(f"""
        <div style="font-size: 40px; animation: blinkRGB 2s step-end infinite; font-weight: bold;">Você acertou! Pontuação: {score}</div>
        <style>
            @keyframes blinkRGB {{
                0% {{color: red;}}
                33% {{color: green;}}
                66% {{color: blue;}}
                100% {{color: red;}}
            }}
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"**Pontuação: {score}**", unsafe_allow_html=True)

# Função principal do app
def main():
    st.title("Quiz com Temporizador")

    # Configuração inicial da pontuação
    if "pontuacao" not in st.session_state:
        st.session_state.pontuacao = 0

    # Verificar se as alternativas já foram embaralhadas
    if "embaralhado" not in st.session_state:
        # Embaralha as opções de resposta apenas uma vez no início
        for questao in quiz_data:
            random.shuffle(questao["opcoes"])
        st.session_state.embaralhado = True

    # Exibe o placar grande no topo
    show_score(st.session_state.pontuacao, is_correct=False)

    # Loop por cada pergunta
    for idx, questao in enumerate(quiz_data):
        st.subheader(f"Pergunta {idx + 1}")
        st.write(questao["pergunta"])

        # Exibe opções e espera resposta
        resposta = st.radio("Escolha uma opção:", questao["opcoes"], key=idx)

        # Temporizador de 5 segundos antes de mostrar o feedback
        if st.button("Responder", key=f"responder_{idx}"):
            st.write("Processando resposta...")

            # Inicia o temporizador de 5 segundos
            for seg in range(5, 0, -1):
                st.write(f"Tempo restante para feedback: {seg} segundos")
                time.sleep(1)

            # Feedback visual após 5 segundos
            if resposta == questao["resposta_correta"]:
                st.success("Correto! 🎉")
                st.session_state.pontuacao += 1
                show_score(st.session_state.pontuacao, is_correct=True)  # Mostra o placar com animação RGB
            else:
                st.error("Incorreto! ❌")
                show_score(st.session_state.pontuacao, is_correct=False)  # Mostra o placar normal

            st.write("---")

    # Exibir pontuação final
    if st.button("Ver Resultado"):
        st.write(f"Você acertou {st.session_state.pontuacao} de {len(quiz_data)} perguntas!")


st.title("Visão de Nós")
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



if __name__ == "__main__":
    main()
