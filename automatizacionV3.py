import streamlit as st
import re
import random

# Funciones
# def extraer_referencias(texto_referencias):
#     url_a_extraer = re.compile(r'\[(\d+)\]\s+.*?(https?://[^\s\]]+)', re.DOTALL | re.IGNORECASE)
#     referencias = {}
#     for match in pattern.finditer(texto_referencias):
#         number = int(match.group(1))
#         url = match.group(2)
#         referencias[number] = url
#     return referencias    

def procesar_referencias(texto_referencias):
    lines = texto_referencias.splitlines()
    patron_a_limpiar = re.compile(r'\b(Available|Disponible en):?\s*|(\.\s*)$', re.IGNORECASE)
    patron_a_extraer = re.compile(r'\[(\d+)\].*?(https?://[^\s\]]+)')
    
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


def procesar_parrafos(text):
    lines = text.split('\n')
    patron_eliminar_figuras = re.compile(r'^(Nota?|Figura|Tabla)(\s+\d+)?.*$')
    filtered_lines = []
    removed_items = []
    paragraph_index = 0
    
    for line in lines:
        if patron_eliminar_figuras.match(line.strip()):
            removed_items.append((paragraph_index, line.strip()))
        elif line.strip():  # Si la línea no está vacía
            paragraph_index += 1
            filtered_lines.append(line)
        else:
            filtered_lines.append(line)

    processed_text = '\n'.join(filtered_lines)
    return processed_text, removed_items

def crear_hipervinculo(text, referencias):
    pattern = re.compile(r'\[([\d,\s]+)\]')
    def replacement(match):
        numbers = match.group(1).split(',')
        links = []
        for number in numbers:
            number = int(number.strip())
            if number in referencias and referencias[number]:
                links.append(f'<a href="{referencias[number]}">[{number}]</a>')
            else:
                links.append(f'[{number}]')
        return ' '.join(links)
    return re.sub(pattern, replacement, text)


# Juego de imágenes
imagenes = [
    ("https://raw.githubusercontent.com/MichaelSuarez0/CeplanCode/main/ceplan_logo.png", 0.80),
    ("https://raw.githubusercontent.com/MichaelSuarez0/CeplanCode/main/con_punche_peru_logo.jpg", 0.20)  # Cambia esto por la URL de tu segunda imagen
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
st.sidebar.header("Aquí podrás copiar fácilmente")
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

    st.text_area("Texto con hipervínculos:", texto_con_hipervinculos, height = 320)
    st.text_area("Referencias limpias", referencias_limpias, height = 290)

    # Filtrar para excluir notas del orden de las figuras
    patron_nota = re.compile(r'Nota')
    items_eliminados_filtrados = [item for item in items_eliminados if not patron_nota.match(item[1])]

    # UI (mostrar orden)
    st.subheader("Orden de las figuras")
    for item in items_eliminados_filtrados:
        st.write(f"**Orden {item[0]}**: {item[1]}")

    # UI (sidebar)
    st.sidebar.write("Texto")
    st.sidebar.code(texto_con_hipervinculos, language = "text")
    st.sidebar.write("Referencias")
    st.sidebar.code(referencias_limpias, language = "text")
