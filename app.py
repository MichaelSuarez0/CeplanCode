# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UBp_YEqulqbpAHzp7id8wZRJP8UiGn3a
"""

import re
import panel as pn

pn.extension()
pn.config.log_level = 'DEBUG'

# Funciones
def extraer_referencias(texto_referencias):
    patron = re.compile(r'\[(\d+)\]\s+.*?(https?://[^\s\]]+)', re.DOTALL | re.IGNORECASE)
    referencias = {}
    for match in patron.finditer(texto_referencias):
        numero = int(match.group(1))
        url = match.group(2)
        # Eliminar punto al final de la URL, si existe
        if url.endswith('.'):
            url = url[:-1]
        referencias[numero] = url
    return referencias

def reemplazar_corchetes(texto, referencias):
    patron = re.compile(r'\[([\d,\s]+)\]')
    def reemplazo(match):
        numeros = match.group(1).split(',')
        links = []
        for numero in numeros:
            numero = int(numero.strip())
            if numero in referencias:
                links.append(f'<a href="{referencias[numero]}">[{numero}]</a>')
            else:
                links.append(f'[{numero}]')
        return ' '.join(links)
    return re.sub(patron, reemplazo, texto)

def añadir_etiquetas_parrafo(texto):
    lineas = texto.splitlines()
    resultado = []
    for i, linea in enumerate(lineas):
        if i == 0:
            resultado.append(f'<p>{linea}')
        else:
            resultado.append(f'</p>\n<p>{linea}')
    resultado.append('</p>')
    return '\n'.join(resultado)

def dividir_en_paneles(texto):
    # Buscar todos los "Figura #" o "Tabla #" al inicio de una línea
    patron = re.compile(r'^(Figura|Tabla) \d+', re.MULTILINE)
    indices = [m.start() for m in patron.finditer(texto)]
    indices.append(len(texto))  # Añadir el final del texto

    paneles = []
    inicio = 0

    for fin in indices[1:]:
        texto_panel = texto[inicio:fin].strip()
        if texto_panel:
            paneles.append(f'<p>{texto_panel}</p>')
        inicio = fin

    return paneles

# Crear los elementos del formulario
texto_principal_input = pn.widgets.TextAreaInput(name='Texto Principal', placeholder='Ingrese el texto principal aquí...', height=200, max_length=100000)
texto_referencias_input = pn.widgets.TextAreaInput(name='Texto de Referencias', placeholder='Ingrese las referencias aquí...', height=200, max_length=100000)
boton_procesar = pn.widgets.Button(name='Procesar', button_type='primary')

# Output del resultado
html_pane = pn.pane.HTML(sizing_mode='stretch_width')
html_output = pn.widgets.TextAreaInput(name='HTML Generado', height=200)

# Estilo CSS básico
css = """
<style>
p {
    text-align: justify;
    line-height: 1.6;
}
a {
    color: blue;
    text-decoration: underline;
}
</style>
"""

# Callback para el botón
import panel as pn
import re

pn.extension()

# Funciones auxiliares (asumiendo que ya las tienes definidas)
# extraer_referencias, reemplazar_corchetes, añadir_etiquetas_parrafo

# Elementos de la interfaz
texto_principal_input = pn.widgets.TextAreaInput(name='Texto Principal', height=200)
texto_referencias_input = pn.widgets.TextAreaInput(name='Texto de Referencias', height=200)
boton_procesar = pn.widgets.Button(name='Procesar', button_type='primary')

css = """
<style>
p {
    text-align: justify;
    line-height: 1.6;
}
a {
    color: blue;
    text-decoration: underline;
}
</style>
"""

import panel as pn
import re

pn.extension()

# Funciones auxiliares (asumiendo que ya las tienes definidas)
# extraer_referencias, reemplazar_corchetes, añadir_etiquetas_parrafo

# Elementos de la interfaz
texto_principal_input = pn.widgets.TextAreaInput(name='Texto Principal', height=200)
texto_referencias_input = pn.widgets.TextAreaInput(name='Texto de Referencias', height=200)
boton_procesar = pn.widgets.Button(name='Procesar', button_type='primary')

# Contenedor para los resultados
resultado_container = pn.Column()

css = """
<style>
p {
    text-align: justify;
    line-height: 1.6;
}
a {
    color: blue;
    text-decoration: underline;
}
</style>
"""

def dividir_en_paneles(texto):
    # Dividir el texto en paneles basados en "Figura #."
    paneles = re.split(r'(Figura \d+\..*?)(?=Figura \d+\.|$)', texto, flags=re.DOTALL)

    # Filtrar paneles vacíos y combinar el texto de la figura con el siguiente panel
    paneles_combinados = []
    for i in range(0, len(paneles), 2):
        panel = paneles[i].strip()
        if i+1 < len(paneles):
            panel += "\n" + paneles[i+1].strip()
        if panel:
            paneles_combinados.append(panel)

    return paneles_combinados


def procesar(event):
    texto_principal = texto_principal_input.value
    texto_referencias = texto_referencias_input.value
    referencias = extraer_referencias(texto_referencias)
    texto_con_links = reemplazar_corchetes(texto_principal, referencias)
    texto_final = añadir_etiquetas_parrafo(texto_con_links)

    # Dividir el texto en paneles
    paneles = dividir_en_paneles(texto_final)

    # Limpiar el contenedor de resultados
    resultado_container.clear()

    # Crear los paneles dinámicamente
    for panel in paneles:
        html_panel = pn.pane.HTML(css + panel, sizing_mode='stretch_width')
        resultado_container.append(html_panel)

    # Añadir el HTML generado al final
    html_output = pn.widgets.TextAreaInput(name='HTML Generado', value=texto_final, height=200)
    resultado_container.append(pn.pane.Markdown("### HTML Generado (copiar desde aquí):"))
    resultado_container.append(html_output)

boton_procesar.on_click(procesar)

# Layout principal
layout = pn.Column(
    texto_principal_input,
    texto_referencias_input,
    boton_procesar,
    resultado_container
)

layout.servable()