import streamlit as st

st.set_page_config(
    page_title = "Contexto",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

st.markdown("<h1 style='font-family: Braggadocio; font-size: 36px; text-align: center;'>Contexto</h1>", unsafe_allow_html=True)
st.header("Noticias")

st.write("Página de entrada")

def linkDeNoticia(link,Noticiatitle):
    linkDeNoticia = f"""
    <a href="{link}" style="font-family: 'Arial', sans-serif; font-size: 24px; text-align: center; display: block;">"{Noticiatitle}"</a>
    """
    return st.markdown(linkDeNoticia, unsafe_allow_html=True)

def linkDeImagen(NoticeImage):
    return st.image(NoticeImage)

def SidebarButton(Category):
    return st.sidebar.button(f"{Category}")

if SidebarButton("ejemplo"):
    a = 5

if SidebarButton("Deportes"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("http://localhost:172.16.5.4:8502","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)

if SidebarButton("Arte"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)

if SidebarButton("Ciencia"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)

if SidebarButton("Política"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)

if SidebarButton("Tecnología"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)

if SidebarButton("Entretenimiento"):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)

else:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","10 Noticias que cambiaron el mundo")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","España vence Inglaterra")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia("https://www.youtube.com/?bp=wgUCEAE%3D","Concierto de Tylor Swift")
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
