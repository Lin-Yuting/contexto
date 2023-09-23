import streamlit as st

st.title("Contexto")
st.header("Noticias")

st.button("Pop Star", type="primary")
if st.button("Lenguaje coloquiar"):
    st.write("1-")
    st.write("¡Atención, amantes de las celebridades! Parece que la estrella del pop internacional, Luna Star, está en medio de un misterioso romance que ha dejado a todos boquiabiertos. ¿La persona afortunada? Nada menos que el famoso chef gourmet, Marco Delicioso.")
    st.write("Los rumores comenzaron cuando Luna y Marco fueron vistos compartiendo una cena íntima en uno de los restaurantes más exclusivos de la ciudad. Testigos aseguran que la química entre ellos era evidente y que pasaron horas riendo y disfrutando de la comida gourmet.")
    st.write("Pero eso no es todo, algunos paparazzi astutos lograron capturarlos en una escapada secreta a una paradisíaca isla tropical. Parece que están decididos a mantener su relación alejada de los reflectores, ¡pero las fotos no mienten!")
    st.write("¿Será este el comienzo de una relación seria o simplemente un romance pasajero? ¡Estaremos atentos para traerte todos los detalles de este intrigante affaire de la alta sociedad!")
    st.write("Recuerda que esto es puramente ficticio y en tono de entretenimiento, ¡no corresponde a una noticia real!")
if st.button('Comic'):
    st.write('---------------')
else:
    st.write("Noticia original-----------------")


st.sidebar.button("Sport")
st.sidebar.button("Art")
st.sidebar.button("Science")
st.sidebar.button("Politic")
st.sidebar.button("Technology")
