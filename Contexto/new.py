import streamlit as st
from gtts import gTTS
from io import BytesIO

st.set_page_config(
    page_title = "Carrera F1 del GP de Japón",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

st.markdown("<h1 style='font-family: Braggadocio; font-size: 36px; text-align: center;'>Carrera F1 del GP de Japón</h1>", unsafe_allow_html=True)
st.image("https://cdn.clarosports.com/clarosports/2023/09/directo-gpjapon-practicas-202438-1024x576.jpg",use_column_width=True)


def Texto(text):
    return st.text(text)

def Audio(text):
        try:
            tts = gTTS(text, lang="es")
            audio_io = BytesIO()
            tts.write_to_fp(audio_io)
            st.audio(audio_io, format="audio/mp3")
        except Exception as e:
            st.error("Error al reproducir el audio.")

st.button("Noticia")
textoO = """La temporada 2023 de Fórmula 1 llega a Japón del 22 al 24 de septiembre. La victoria de Carlos Sainz en Singapur confirmó la mejora de Ferrari 
en este último mes y puso un alto al hasta entonces dominio de Red Bull. Ahora, la escudería italiana busca seguir sumando buenos resultados para desplazar
a Mercedes del segundo lugar en el campeonato de constructores.
Por otro lado, los pilotos de Red Bull llegan con ganas de revancha,
después de haber tenido un flojo fin de semana la fecha anterior. Max Verstappen vio interrumpido su récord de diez victorias consecutivas e intentará
volver a pararse en lo más alto del podio en el Circuito de Suzuka. A lo mismo aspira su compañero de equipo, Checo Pérez, que no gana una carrera desde
el 30 de abril, cuando se impuso en el Gran Premio de Azerbaiyán."""
Texto(textoO)
Audio(textoO)

if st.button("Contexto"):
    textoC = """La Fórmula 1 está que arde en Japón esta semana, del 22 al 24 de septiembre. Ferrari está en racha después de que Carlos Sainz ganara en Singapur, 
    lo que rompió el reinado de Red Bull. Ahora, los chicos de Ferrari quieren subir aún más en la tabla para dejar atrás a Mercedes.
    Por otro lado, los pilotos de Red Bull están sedientos de revancha después de un fin de semana flojo en la última carrera. Max Verstappen ya no lleva diez 
    victorias seguidas, pero espera volver a la cima en el Circuito de Suzuka. Lo mismo va para su compañero, Checo Pérez, que no ha ganado desde abril en Azerbaiyán.
    ¡Está que arde la pista en Japón!"""
    Texto(textoC)
    Audio(textoC)
