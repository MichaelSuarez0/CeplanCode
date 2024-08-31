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
    global debug_output
    debug_output.value += "\nEntering dividir_en_paneles function"
    debug_output.value += f"\nInput text length: {len(texto)}"

    # Buscar todos los "Figura #" o "Tabla #" al inicio de una línea, con <p> tag
    patron = re.compile(r'^<p>(Figura|Tabla) \d+', re.MULTILINE)
    matches = list(patron.finditer(texto))

    debug_output.value += f"\nFound {len(matches)} Figura/Tabla markers"
    for i, match in enumerate(matches):
        debug_output.value += f"\nMarker {i+1} at position {match.start()}: {match.group()}"

    if not matches:
        debug_output.value += "\nNo Figura/Tabla markers found, using entire text as one panel"
        return [texto]

    paneles = []

    # Panel before the first marker
    paneles.append(texto[:matches[0].start()].strip())

    # Panels between markers
    for i in range(len(matches) - 1):
        paneles.append(texto[matches[i].start():matches[i+1].start()].strip())

    # Panel after the last marker
    paneles.append(texto[matches[-1].start():].strip())

    debug_output.value += f"\nCreated {len(paneles)} panels"
    return paneles

# Elementos de la interfaz
texto_principal_input = pn.widgets.TextAreaInput(name='Texto Principal', height=250, width=800, max_length=1000000)
texto_referencias_input = pn.widgets.TextAreaInput(name='Texto de Referencias', height=250, width=800, max_length=1000000)
boton_procesar = pn.widgets.Button(name='Procesar', button_type='primary')

# Contenedor para los resultados
resultado_container = pn.Column()

# Debug output
debug_output = pn.widgets.StaticText(value="Debug output will appear here")

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

def procesar(event):
    global debug_output
    debug_output.value = "Procesamiento iniciado..."

    texto_principal = texto_principal_input.value
    texto_referencias = texto_referencias_input.value

    debug_output.value += f"\nLongitud del texto: {len(texto_principal)}, Longitud de referencias: {len(texto_referencias)}"

    referencias = extraer_referencias(texto_referencias)
    debug_output.value += f"\nSe extrajeron {len(referencias)} referencias"

    texto_con_links = reemplazar_corchetes(texto_principal, referencias)
    debug_output.value += f"\nLongitud del texto con enlaces: {len(texto_con_links)}"

    texto_final = añadir_etiquetas_parrafo(texto_con_links)
    debug_output.value += f"\nLongitud del texto final: {len(texto_final)}"

    # Limpiar paneles existentes
    resultado_container.clear()
    debug_output.value += "\nSe limpió el contenedor de resultados"

    # Llamar explícitamente a dividir_en_paneles
    debug_output.value += "\nLlamando a dividir_en_paneles..."
    paneles = dividir_en_paneles(texto_final)
    debug_output.value += f"\nSe dividió en {len(paneles)} paneles"

    # Imprimir el contenido de cada panel
    #for i, panel in enumerate(paneles):
    #    debug_output.value += f"\nContenido del panel {i+1} (primeros 100 caracteres): {panel[:100]}"

    if len(paneles) == 0:
        debug_output.value += "\nNo se crearon paneles, usando todo el texto como un solo panel"
        paneles = [texto_final]

    # Crear los paneles dinámicamente
    for i, panel in enumerate(paneles):
        html_output = pn.widgets.TextAreaInput(
            name=f'Panel {i+1}',
            value=panel,
            height=200,
            sizing_mode='stretch_width'
        )
        resultado_container.append(html_output)
        debug_output.value += f"\nSe añadió el panel {i+1} con longitud {len(panel)}"

    debug_output.value += "\nProcesamiento completado"

boton_procesar.on_click(procesar)

layout = pn.Column(
    texto_principal_input,
    texto_referencias_input,
    boton_procesar,
    debug_output,
    resultado_container
)

layout.servable()