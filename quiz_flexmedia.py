from PIL import Image
import streamlit as st

st.set_page_config(
    page_title="Quiz Totem FlexMedia",
    page_icon="logo_flexmedia.png",
    layout="centered"
)

logo = Image.open("logo_flexmedia.png")
st.image(logo, width=150)

st.title("🎯 Quiz Interativo - Totem FlexMedia")
st.write("Teste seus conhecimentos sobre o projeto Totem FlexMedia!")

VICTORY_SOUND = """..."""  
NEGATIVE_SOUND = """..."""  

perguntas = [
    ("O Totem FlexMedia foi criado para:", 
     ["Jogar online", "Exibir e cadastrar informações interativas", "Servir como caixa eletrônico", "Medir temperatura corporal"], 1),
    ("Em qual linguagem o Totem foi programado?", 
     ["C++", "Java", "Python", "HTML"], 2),
    ("Qual biblioteca é usada para criar pausas no tempo?", 
     ["sys", "time", "os", "math"], 1),
    ("O tipo 'Cultural' é um exemplo de:", 
     ["Função Python", "Tipo permitido no cadastro", "Módulo externo", "Comando de sistema"], 1),
    ("O comando que limpa a tela no Windows é:", 
     ["clear", "cls", "clean", "wipe"], 1),
    ("O Totem FlexMedia é um:", 
     ["Jogo educativo", "Protótipo de totem interativo", "Site informativo", "Banco de dados"], 1),
    ("O menu principal oferece quantas opções?", 
     ["2", "3", "4", "5"], 1),
    ("Qual biblioteca foi usada para criar a interface do quiz?", 
     ["Tkinter", "PyQt", "Streamlit", "Dash"], 2),
    ("O que acontece ao finalizar o quiz?", 
     ["Nada", "O app fecha automaticamente", "É criado um arquivo 'quiz_finalizado.txt'", "O sistema reinicia"], 2),
    ("O som de vitória é armazenado em que formato?", 
     ["MP3", "WAV", "OGG", "MIDI"], 1),
]

for i in range(1, len(perguntas)+1):
    if f"q{i}" not in st.session_state:
        st.session_state[f"q{i}"] = None

if "finalizado" not in st.session_state:
    st.session_state.finalizado = False

pontos = 0

for i, (pergunta, opcoes, correta) in enumerate(perguntas, start=1):
    st.subheader(f"{i}. {pergunta}")

    if not st.session_state.finalizado:
        st.radio("", opcoes, key=f"q{i}")
    else:
        user_resp = st.session_state[f"q{i}"]
        for idx, opcao in enumerate(opcoes):
            marcador = "⚪"
            estilo = ""

            if opcao == user_resp:
                marcador = "⚫"

            if idx == correta:
                estilo = "<span style='color:limegreen;'>✅ Correto</span>"
            elif opcao == user_resp:
                estilo = "<span style='color:red;'>❌ Errado</span>"

            if opcao == user_resp and idx == correta:
                pontos += 1

            st.markdown(f"{marcador} {opcao} {estilo}", unsafe_allow_html=True)

    st.write("---")

if not st.session_state.finalizado:
    if st.button("✅ Finalizar Quiz"):
        st.session_state.finalizado = True
        st.rerun()
else:
    st.subheader("🎯 Resultado Final")
    total = len(perguntas)

    if pontos >= 6:
        st.balloons()
        st.success(f"🎉 Parabéns! Você acertou {pontos} de {total} perguntas! 🧠💡")
        st.info("Acima da média! Você finalizou o quiz com sucesso! 🚀")
        
        # Cria arquivo para sinalizar finalização
        with open("quiz_finalizado.txt", "w") as f:
            f.write("ok")
        
        st.success("🎉 Quiz finalizado com sucesso! Você pode fechar esta aba.")

        st.markdown(f"""
        <audio autoplay>
            <source src="data:audio/wav;base64,{VICTORY_SOUND}" type="audio/wav">
        </audio>
        """, unsafe_allow_html=True)

    else:
        st.error(f"😞 Você acertou apenas {pontos} de {total} perguntas.")
        st.warning("Ficou abaixo da média... tente novamente! 💪")
        st.image("https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif", width=200)
        st.markdown(f"""
        <audio autoplay>
            <source src="data:audio/wav;base64,{NEGATIVE_SOUND}" type="audio/wav">
        </audio>
        """, unsafe_allow_html=True)

        if st.button("🔁 Tentar Novamente"):
            for i in range(1, len(perguntas)+1):
                st.session_state[f"q{i}"] = None
            st.session_state.finalizado = False
            st.rerun()
