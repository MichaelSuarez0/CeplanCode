import re
import random
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="App_Observatorio",
    page_icon="✏️",
)

# Función para procesar referencias y extraer URLs
def procesar_referencias(texto_referencias):
    lines = texto_referencias.splitlines()
    patron_a_limpiar = re.compile(r'\bAvailable:?\s*|(\.\s*)$', re.IGNORECASE)
    patron_a_extraer = re.compile(r'\[(\d+)\].*?(https?://[^\s\[\]]+)')

    referencias_limpias = []
    referencias_internas = {}

    for line in lines:
        referencia_limpia = re.sub(patron_a_limpiar, '', line).strip()
        referencias_limpias.append(referencia_limpia)

        match = patron_a_extraer.search(referencia_limpia)
        if match:
            numero = int(match.group(1))
            url = match.group(2)
            referencias_internas[numero] = url

    texto_limpio = '\n'.join(referencias_limpias)
    return texto_limpio, referencias_internas

# Función para procesar párrafos y eliminar los que comienzan con "Tabla" hasta que se encuentre "Nota"
def procesar_parrafos(text):
    paragraphs = text.split('\n')
    patron_eliminar_figuras = re.compile(r'^(Nota?|Figura)(\s+\d+)?.*$')
    patron_tabla = re.compile(r'^Tabla(\s+\d+)?.*$', re.IGNORECASE)
    patron_nota = re.compile(r'^Nota(\s*)?.*$', re.IGNORECASE)

    filtered_lines = []
    removed_items = []
    eliminar = False
    paragraph_index = 0

    for paragraph in paragraphs:
        paragraph = paragraph.strip()  # Eliminar espacios en blanco al principio y al final

        if patron_tabla.match(paragraph):
            removed_items.append((paragraph_index, paragraph))
            eliminar = True  # Inicia el proceso de eliminación
            continue  # Saltar este párrafo

        if patron_nota.match(paragraph):
            eliminar = False  # Termina el proceso de eliminación
            continue  # Saltar este párrafo y no eliminarlo

        if eliminar:
            continue  # Saltar párrafos sin modificar el índice ni agregarlos a removed_items

        # Asegurarse de que el párrafo termine con un punto final
        if paragraph and not paragraph.endswith('.'):
            paragraph += '.'  # Añadir un punto final si no lo tiene

        if patron_eliminar_figuras.match(paragraph):
            removed_items.append((paragraph_index, paragraph))
        elif paragraph:  # Si el párrafo existe y no está vacío
            filtered_lines.append(paragraph)
            paragraph_index += 1

    # Unir los párrafos y eliminar solo el último punto, si existe
    processed_text = '\n'.join(filtered_lines)
    if processed_text.endswith('.'):
        processed_text = processed_text[:-1]  # Eliminar solo el punto final del último párrafo (el Obs lo genera automáticamente)

    # Normalizar caracteres especiales
    processed_text = re.sub(
        r'[⁰¹²³⁴⁵⁶⁷⁸⁹₀₁₂₃₄₅₆₇₈₉]',
        lambda m: {
            '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5',
            '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '₀': '0', '₁': '1',
            '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6', '₇': '7',
            '₈': '8', '₉': '9'
        }[m.group(0)],
        processed_text
    )

    return processed_text, removed_items

# Función para crear hipervínculos en el texto
def crear_hipervinculo(text, referencias):
    pattern = re.compile(r'\[([\d,\s]+)\]')

    def replacement(match):
        numbers = match.group(1).split(',')
        links = []
        for number in numbers:
            number = int(number.strip())
            if number in referencias and referencias[number]:
                links.append(f'<a href="{referencias[number]}" target="_blank">[{number}]</a>')
            else:
                links.append(f'[{number}]')
        return ' '.join(links)

    return re.sub(pattern, replacement, text)

# Juego de imágenes
imagenes = [
    ("https://raw.githubusercontent.com/MichaelSuarez0/CeplanCode/main/imagenes/ceplan_logo.png", 0.85),
    ("https://raw.githubusercontent.com/MichaelSuarez0/CeplanCode/main/imagenes/con_punche_peru_logo.jpg", 0.15)
]

# Genera un número aleatorio solo una vez
numero_aleatorio = random.random()

# Suma acumulativa de probabilidades para selección correcta
suma_probabilidad = 0
url = None

for imagen_url, probabilidad in imagenes:
    suma_probabilidad += probabilidad
    if numero_aleatorio < suma_probabilidad:
        url = imagen_url
        break

# Streamlit UI
st.sidebar.image(url, width=280)
st.sidebar.write(numero_aleatorio)
st.sidebar.header("Aquí podrás copiar pasando tu cursor")
st.title('Aplicación para procesar texto (Observatorio)')

# Input fields
input_text_main = st.text_area('Inserta el texto aquí', height=200)
input_text_referencias = st.text_area('Inserta las referencias aquí', height=190)

boton_procesar = st.button('Procesar')

st.subheader("Aquí podrás verificar")

if boton_procesar:
    referencias_limpias, referencias_internas = procesar_referencias(input_text_referencias)
    texto_procesado, items_eliminados = procesar_parrafos(input_text_main)
    texto_con_hipervinculos = crear_hipervinculo(texto_procesado, referencias_internas)

    texto_centrado = f"""
    <div style="text-align: center;">
    {texto_con_hipervinculos}
    </div>
    """

    st.text_area("Texto con hipervínculos:", texto_con_hipervinculos, height=350)
    st.text_area("Referencias limpias", referencias_limpias, height=290)

    # Filtrar para excluir notas del orden de las figuras
    patron_nota = re.compile(r'Nota')
    items_eliminados_filtrados = [item for item in items_eliminados if not patron_nota.match(item[1])]

    # UI (mostrar orden)
    st.subheader("Orden de las figuras")
    for item in items_eliminados_filtrados:
        st.write(f"**Orden {item[0]}**: *{item[1]}*")

    # UI (sidebar)
    st.sidebar.write("Texto")
    st.sidebar.code(texto_con_hipervinculos, language="text")
    st.sidebar.write("Referencias")
    st.sidebar.code(referencias_limpias, language="text")
