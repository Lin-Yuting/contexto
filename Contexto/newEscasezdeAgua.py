import streamlit as st
from gtts import gTTS
from io import BytesIO

st.set_page_config(
    page_title = "La crisis de agua en Nuevo León",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

st.markdown("<h1 style='font-family: Braggadocio; font-size: 36px; text-align: center;'>La crisis de agua en Nuevo León</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>Autor: Javier Treviño, X @javier_trevino</h1>", unsafe_allow_html=True) 
st.image("https://www.sdpnoticias.com/resizer/dcUT_j0QwFSIHhnVcbRoNUpRHRM=/1440x810/filters:format(jpg):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/sdpnoticias/SP2AVFZLHBCZFKOPKPZ7H4JP5Q.jpeg",use_column_width=True)
st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>Gabriela Pérez. Presa en Nuevo León</h1>", unsafe_allow_html=True) 

def linkNoticia(link,Noticiatitle):
    linkDeNoticia = f"""
    <a href="{link}" style="font-family: 'Arial', sans-serif; font-size: 24px; text-align: center; display: block;">"{Noticiatitle}"</a>
    """
    return st.markdown(linkDeNoticia, unsafe_allow_html=True)

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

st.button("Contexto")
textoC = """¡Atención, amigos! Monterrey acaba de ser nombrada la mejor ciudad para vivir en México, ¡qué orgullo! Pero, ¿adivinen qué? También estamos teniendo un 
problemilla con el agua, así que agárrense.

Resulta que según un estudio de The Economist, Monterrey se llevó el primer lugar como la ciudad más chida para vivir en México. Se destacó por ser estable, 
con mucha cultura y entretenimiento, buena infraestructura y flexibilidad durante la pandemia. Pero no todo es fiesta, porque estamos batallando con la falta de agua.
El crecimiento de la población, la economía y el cambio climático están presionando nuestro suministro de agua. Y no, la lluvia no va a salvarnos para siempre. 
Necesitamos un plan completo para asegurarnos de tener suficiente agua.

La crisis del agua no es solo aquí, es un problema global. Así que, necesitamos que el gobierno y todos nosotros actuemos rápido. Debemos ayudar a las familias sin 
agua con camiones cisterna, y también aprender de otras ciudades que resolvieron problemas similares.

¿Cuáles son las soluciones que podemos considerar? ¡Aquí van algunas ideas para salvar el día!

Involucrar a todos: Hagan fila, servidores públicos, empresas y sociedad civil. Necesitamos evaluar riesgos, desarrollar estrategias y trabajar juntos.
Tarifas inteligentes: Si usas más agua, pagarás más. Esto fomenta la conservación.

¡A reciclar agua!: Usemos aguas residuales tratadas, así no desperdiciamos agua fresca.

Monitoreo constante: Vigilemos de cerca la calidad del agua y tomemos medidas rápidas.
Agua de mar y desalinización: Consideremos usar agua salobre y desalar agua de mar si es necesario.

No desperdiciemos: Gastemos agua sabiamente, desde el riego hasta la industria.

Cooperación: Trabajemos con otras ciudades y estados para soluciones comunes.

¡Manos a la obra! Sigamos disfrutando de vivir en la mejor ciudad de México y trabajemos juntos para asegurar un futuro húmedo y próspero para Monterrey. 
¡Vamos por más, Monterrey!
"""

Texto(textoC)
Audio(textoC)

if st.button("Noticia Original"):
    st.text("Para más información consulta el artículo original: ")
    linkNoticia("https://www.sdpnoticias.com/opinion/la-crisis-del-agua-en-nuevo-leon/'","La crisis de agua en Nuevo León")
    st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>Treviño, J. (2022, June 26). La crisis del agua en Nuevo León. Sdpnoticias.</h1>", unsafe_allow_html=True) 

