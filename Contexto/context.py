import streamlit as st

st.set_page_config(
    page_title = "Contexto",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

st.markdown("<h1 style='font-family: Braggadocio; font-size: 36px; text-align: center;'>Contexto</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='font-family: Arial; font-size: 30px; text-align: center;'>Noticas Recientes</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='font-family: Arial; font-size: 24px; text-align: center;'>Contexto de Noticas</h1>", unsafe_allow_html=True)

def linkDeNoticia(link,Noticiatitle):
    linkDeNoticia = f"""
    <a href="{link}" style="font-family: 'Arial', sans-serif; font-size: 24px; text-align: center; display: block;">"{Noticiatitle}"</a>
    """
    return st.markdown(linkDeNoticia, unsafe_allow_html=True)

def linkDeImagen(NoticeImage):
    return st.image(NoticeImage)

def SidebarButton(Category):
    return st.sidebar.button(f"{Category}")

if SidebarButton("Deportes"):
    col1, col2, col3 = st.columns(3)
    with col1:
        linkDeImagen("https://cdn.clarosports.com/clarosports/2023/09/directo-gpjapon-practicas-202438-1024x576.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","Carrera F1 del GP de Japón")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        linkDeImagen("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        linkDeImagen("https://st1.uvnimg.com/3c/a6/921400d0499cb2980b77c519307e/futbol-generic-entry-point.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","La fuerza del fútbol")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        linkDeImagen("https://cdn.clarosports.com/clarosports/2023/09/directo-gpjapon-practicas-202438-1024x576.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","Carrera F1 del GP de Japón")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        linkDeImagen("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        linkDeImagen("https://st1.uvnimg.com/3c/a6/921400d0499cb2980b77c519307e/futbol-generic-entry-point.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","La fuerza del fútbol")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)

if SidebarButton("Arte"):
    col1, col2, col3 = st.columns(3)
    with col1:
        linkDeImagen("https://www.revistaestilo.net/binrepository/1920x1005/0c0/0d0/none/179468266/TSSU/devon-rodriguez-el-hondureno-que-del_3490122_20230118131320.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","De TikTok a la galería")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        linkDeImagen("https://terapiasderelajacionmedellin.com/wp-content/uploads/2022/07/Plaza-Botero.webp")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","¿Cómo está la plaza Botero de Medellín?")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        linkDeImagen("https://cnnespanol.cnn.com/wp-content/uploads/2023/09/230913032928-01-picasso-masterpiece-auction-full-169.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","Pintura de Picasso podría alcanzar una suma multimillonaria")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        linkDeImagen("https://www.revistaestilo.net/binrepository/1920x1005/0c0/0d0/none/179468266/TSSU/devon-rodriguez-el-hondureno-que-del_3490122_20230118131320.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","De TikTok a la galería")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        linkDeImagen("https://terapiasderelajacionmedellin.com/wp-content/uploads/2022/07/Plaza-Botero.webp")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","¿Cómo está la plaza Botero de Medellín?")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        linkDeImagen("https://cnnespanol.cnn.com/wp-content/uploads/2023/09/230913032928-01-picasso-masterpiece-auction-full-169.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","Pintura de Picasso podría alcanzar una suma multimillonaria")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)

if SidebarButton("Ciencia"):
    col1, col2, col3 = st.columns(3)
    with col1:
        linkDeImagen("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        linkDeImagen("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        linkDeImagen("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","Concierto de Taylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        linkDeImagen("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        linkDeImagen("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        linkDeImagen("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","Concierto de Taylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)

if SidebarButton("Política"):
    col1, col2, col3 = st.columns(3)
    with col1:
        linkDeImagen("https://www.sdpnoticias.com/resizer/dcUT_j0QwFSIHhnVcbRoNUpRHRM=/1440x810/filters:format(jpg):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/sdpnoticias/SP2AVFZLHBCZFKOPKPZ7H4JP5Q.jpeg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","La crisis de agua en Nuevo León")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        linkDeImagen("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        linkDeImagen("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","Concierto de Taylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        linkDeImagen("https://www.sdpnoticias.com/resizer/dcUT_j0QwFSIHhnVcbRoNUpRHRM=/1440x810/filters:format(jpg):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/sdpnoticias/SP2AVFZLHBCZFKOPKPZ7H4JP5Q.jpeg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","La crisis de agua en Nuevo León")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        linkDeImagen("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        linkDeImagen("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","Concierto de Taylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)

if SidebarButton("Tecnología"):
    col1, col2, col3 = st.columns(3)
    with col1:
        linkDeImagen("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        linkDeImagen("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        linkDeImagen("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","Concierto de Taylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        linkDeImagen("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        linkDeImagen("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        linkDeImagen("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","Concierto de Taylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)

if SidebarButton("Entretenimiento"):
    col1, col2, col3 = st.columns(3)
    with col1:
        linkDeImagen("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","La crisis de agua en Nuevo León")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        linkDeImagen("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        linkDeImagen("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","Concierto de Taylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        linkDeImagen("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        linkDeImagen("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        linkDeImagen("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","Concierto de Taylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
else:
    col1, col2, col3 = st.columns(3)
    with col1:
        linkDeImagen("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        linkDeImagen("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        linkDeImagen("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://stunning-xylophone-5gqx59prvg6xhqxr-8503.app.github.dev/","Concierto de Taylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)