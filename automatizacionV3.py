import streamlit as st
import re

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


def crear_hipervinculo(text, referencias):
    pattern = re.compile(r'\[([\d,\s]+)\]')
    def replacement(match):
        numbers = match.group(1).split(',')
        links = []
        for number in numbers:
            number = int(number.strip())
            if number in referencias and referencias[number]:  # Verifica si el número existe y tiene una URL asociada
                links.append(f'<a href="{referencias[number]}">[{number}]</a>')
            else:
                links.append(f'[{number}]')
        return ' '.join(links)
    return re.sub(pattern, replacement, text)

# Streamlit UI
st.sidebar.image(r"C:\Users\SALVADOR\OneDrive\CEPLAN\CeplanPythonCode\logo.png", width = 280)
st.sidebar.header("Aquí podrás copiar")
st.title('Aplicación para procesar texto (Observatorio)')


# Input fields
input_text_main = st.text_area('Inserta el texto aquí', height=200)
input_text_referencias = st.text_area('Inserta las referencias aquí', height=190)

boton_procesar = st.button('Procesar')

st.header("Aquí podrás verificar")

if boton_procesar:
    referencias_limpias, referencias_internas = procesar_referencias(input_text_referencias)
    texto_con_hipervinculos = crear_hipervinculo(input_text_main, referencias_internas)
    st.text_area("Texto con hipervínculos:", texto_con_hipervinculos, height = 300)
    st.text_area("Referencias limpias", referencias_limpias, height = 300)
    st.sidebar.write("Texto")
    st.sidebar.code(texto_con_hipervinculos, language = "text")
    st.sidebar.write("Referencias")
    st.sidebar.code(referencias_limpias, language = "text")
