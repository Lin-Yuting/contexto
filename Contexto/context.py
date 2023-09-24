import streamlit as st

st.set_page_config(
    page_title = "Contexto",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

st.markdown("<h1 style='font-family: Braggadocio; font-size: 36px; text-align: center;'>Contexto</h1>", unsafe_allow_html=True)
st.header("Noticias")

st.write("Página de entrada")


if st.sidebar.button("Deportes"):
    st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
st.sidebar.button("Arte")
st.sidebar.button("Ciencia")
st.sidebar.button("Política")
st.sidebar.button("Tecnología")
if st.sidebar.button("Entretenimiento"):
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia = """
            <a href="https://www.youtube.com/?bp=wgUCEAE%3D" style = "font-family: 'Arial',sans-serif; font-size: 24px; text-align: center; display: block;"> 10 Noticias que cambiaron el mundo </a>
        """
        st.markdown(linkDeNoticia,unsafe_allow_html=True)
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col2:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia2 = """
            <a href="https://www.youtube.com/?bp=wgUCEAE%3D" style = "font-family: 'Arial',sans-serif; font-size: 24px; text-align: center; display: block;"> España vence a Inglaterra </a>
        """
        st.markdown(linkDeNoticia2,unsafe_allow_html=True)
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col3:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia3 = """
            <a href="https://www.youtube.com/?bp=wgUCEAE%3D" style = "font-family: 'Arial',sans-serif; font-size: 24px; text-align: center; display: block;"> Conciero de Taylor Swift </a>
        """
        st.markdown(linkDeNoticia3,unsafe_allow_html=True)
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    
    st.text("--------------------------------------------------------------------------------------------------------------")

    col4, col5, col6 = st.columns(3)
    with col4:
        st.image("https://media.datacenterdynamics.com/media/images/Extra.original.jpg")
        linkDeNoticia4 = """
            <a href="https://www.youtube.com/?bp=wgUCEAE%3D" style = "font-family: 'Arial',sans-serif; font-size: 24px; text-align: center; display: block;"> 10 Noticias que cambiaron el mundo </a>
        """
        st.markdown(linkDeNoticia4,unsafe_allow_html=True)
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col5:
        st.image("https://cnnespanol.cnn.com/wp-content/uploads/2023/08/GettyImages-1627311232-e1692541636956.jpg?quality=100&strip=info")
        linkDeNoticia5 = """
            <a href="https://www.youtube.com/?bp=wgUCEAE%3D" style = "font-family: 'Arial',sans-serif; font-size: 24px; text-align: center; display: block;"> España vence a Inglaterra </a>
        """
        st.markdown(linkDeNoticia5,unsafe_allow_html=True)
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
    with col6:
        st.image("https://imagenes.elpais.com/resizer/RmQ4R6zkGe3on3ezyvO12i6kZBs=/1200x0/cloudfront-eu-central-1.images.arcpublishing.com/prisa/NPQ3SK5STVDQBMUYSGT6SKBN7Q.jpg")
        linkDeNoticia6 = """
            <a href="https://www.youtube.com/?bp=wgUCEAE%3D" style = "font-family: 'Arial',sans-serif; font-size: 24px; text-align: center; display: block;"> Conciero de Taylor Swift </a>
        """
        st.markdown(linkDeNoticia6,unsafe_allow_html=True)
        st.markdown("<h1 style='font-family: Arial; font-size: 12px; text-align: center;'>ooooooooooooooooooooooooooooooooooooo</h1>", unsafe_allow_html=True)
