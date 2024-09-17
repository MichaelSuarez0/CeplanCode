import streamlit as st
import re
import random

st.set_page_config(
    page_title="Preguntas frecuentes",
    page_icon="👋",
)

# Título de la página
st.title('Preguntas Frecuentes')

# Descripción introductoria
st.markdown("""
Bienvenido a la sección de Preguntas Frecuentes. Aquí encontrarás respuestas a las preguntas más comunes. Si no encuentras lo que buscas, no dudes en contactarnos.
""")


# Crear un diccionario con preguntas y respuestas en formato Markdown con viñetas
faq_app = {
    "**¿Qué es esto?**": """
Para que los visitantes del Observatorio Nacional de Prospectiva sean redirigidos a la página web correspondiente luego de hacer clic a una cita, es necesario agregar un formato html a las citas.
Normalmente, los encargados de actualizar el Observatorio lo hacemos de forma manual, una por una, lo cual es una tarea tediosa y repetitiva.
Esta aplicación, entre otras funciones, se encarga de automatizar este proceso 🙂.
""",
"**¿Qué cambios le hace a mi texto, exactamente?**": """
La función primaria de la aplicación es añadir el formato correspondiente para generar hipervínculos en las citas.
No obstante, la aplicación tiene otras mejoras de calidad de vida. Esta es una lista completa de los cambios que hace:
- Al contenido
    - Añade el formato correspondiente (html) para generar hipervínculos en las citas.
    - Elimina las líneas que comienzan con Figura, Tabla o Nota, ya que esto se coloca en una sección aparte en el Observatorio.
    - Devuelve el orden en el cual poner las Figuras y Tablas.
    - Elimina espacios en blanco adicionales al final de un párrafo que pueden afectar la funcionalidad "Nuevo Bloque" del Observatorio.
- A las referencias
    - Quita los puntos finales a los links que aparecen por defecto al ser copiados de Word.
    - Elimina los "Available: " o "Disponible en ".
""",
    "**Ok, quiero actualizar una ficha, ¿qué requisitos o qué debo tomar en cuenta antes de copiar mi texto?**": """
- Sobre tu texto:
    - Debes eliminar el título y la sumilla antes de insertar el texto, ya que ellos se modifican en otro apartado del Observatorio.
    - Debes eliminar los gráficos y las tablas, ya que estos se agregan en la sección de gráficos del Observatorio.
- Sobre tus referencias
    - Deben estar en formato IEE.
    - Idealmente, deben tener un link visible. 
        - Para ello, el tipo de fuente bibliográfica de tus referencias debe ser o "Sitio Web" o "Documento de Sitio Web". 
        - No se generarán hipervínculos para las citas que no tienen link, así que se quedarán como texto.
""",
    "**Solo quiero hacer cambios menores a una ficha, ¿también me ayudará esta aplicación?**": """
Depende de la magnitud de los cambios, pero por lo general no. Correcciones ortográficas . Agregar párrafos o citas
""",
 "**¿No es mejor que se integre una funcionalidad así dentro del código del Observatorio?**": """
Sí, eso es lo ideal, pero eso escapa de mis habilidades.
""",
"**Tengo o he encontrado un problema con la aplicación y no sé cómo resolverlo**": """
Oh no. Por favor contáctame 
- Teams: Michael Salvador Suárez Patilongo
- Correo: msuarez@ceplan.gob.pe
""",
"**¿Cómo funciona esta aplicación? ¿Con qué lenguaje?**": """
Tanto el funcionamiento interno (backend) como el desarrollo web (frontend) fue hecho con Python.
En particular, el frontend se desarrolló con la librería Streamlit.
""",
"**Me interesa ver el source code**": """
¡Genial! Lo puedes ver en mi repositorio de Github: https://github.com/MichaelSuarez0/CeplanCode

"""

}

faq_obs = {
    "**¿No es mejor que se integre una funcionalidad así dentro del código del Observatorio?**": """
Sí, eso es lo ideal, pero eso escapa de mis habilidades.
""",
    "Tengo un problema para subir ": """
- Ve a la sección 'Mis pedidos' en tu perfil.
- Allí podrás ver el estado y detalles de tus pedidos.
""",
    "¿Cómo contacto con el soporte?": """
- Puedes contactar con nuestro soporte a través de la página de 'Contacto'.
- También puedes enviar un correo electrónico a soporte@ejemplo.com.
"""
}

# Sección de preguntas frecuentes
st.header("🔍 Preguntas y Respuestas")
st.subheader("Sobre la aplicación")
# Mostrar preguntas y respuestas
for question, answer in faq_app.items():
    with st.expander(question):
        st.markdown(answer)

#st.subheader("Sobre el Observatorio")
# Mostrar preguntas y respuestas
#for question, answer in faq_obs.items():
#    with st.expander(question):
#        st.markdown(answer)


# Sección de búsqueda de preguntas
st.header("🔎 Buscar Preguntas")

search_query = st.text_input("Introduce tu pregunta aquí:", "")

if search_query:
    matching_faq = {q: a for q, a in faq_app.items() if search_query.lower() in q.lower()}
    if matching_faq:
        for question, answer in matching_faq.items():
            with st.expander(question):
                st.markdown(answer)
    else:
        st.write("No se encontraron coincidencias. Por favor, intenta con otras palabras clave.")

# Sección para hacer preguntas adicionales
st.header("❓ ¿No encontraste tu respuesta?")

additional_question = st.text_area("Escribe tu pregunta aquí:", "")

if st.button("Enviar Pregunta"):
    if additional_question:
        st.success("Gracias por tu pregunta. Nos pondremos en contacto contigo pronto.")
    else:
        st.warning("Por favor, escribe tu pregunta antes de enviarla.")

# Nota de cierre
st.markdown("""
Si tienes más dudas o necesitas asistencia adicional, no dudes en **contactarnos**. Estamos aquí para ayudarte.
""")
