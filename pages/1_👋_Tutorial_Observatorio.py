import streamlit as st

st.set_page_config(
    page_title="Tutorial Observatorio",
    page_icon="👋",
)

st.title('Guía para publicar en el Observatorio')


# Markdown content
markdown_content = """
# Introducción

Esta es una guía para publicar en el Observatorio.
## Paso 1: Preparar tu contenido

Asegúrate de que tu contenido esté listo para ser publicado. Esto incluye:

- Revisar el contenido
- Formatear el texto
- Incluir imágenes y gráficos relevantes

## Paso 2: Publicar tu contenido

Sigue estos pasos para publicar tu contenido:

1. **Inicia sesión** en el sistema de publicación.
2. **Selecciona** el tipo de publicación.
3. **Carga** tu documento preparado.
4. **Revisa** la vista previa.
5. **Confirma** la publicación.

## Consejos útiles

- Usa un lenguaje claro y conciso.
- Verifica todos los enlaces y referencias.
- Pide retroalimentación antes de la publicación final.

## Contacto

Si tienes alguna pregunta o necesitas ayuda, no dudes en contactarme, para eso estoy :)

---

¡Buena suerte con tu publicación!
"""

st.markdown(markdown_content)

placeholder_text= '''
Para el año 2035, se proyecta que alrededor del 35 % de los adultos peruanos serán obesos. Según datos de 2023, el Perú experimentó un incremento significativo en las tasas de obesidad y sobrepeso en la población adulta: la obesidad afectaba al 26,3 % de la población adulta en las zonas urbanas, y al 14 % de la población en las zonas rurales. Asimismo, el sobrepeso afectaba al 38,2 % de la población urbana y al 32,9 % de la población rural. Los niveles más altos se registraron en Lima Metropolitana, donde el 27,5 % de los habitantes padecía obesidad y el 39,6 % tenía sobrepeso. A escala global, se espera que más del 50 % de la población mundial se vea afectada por el sobrepeso y la obesidad.
El sobrepeso y la obesidad en el Perú representan un creciente desafío para la salud pública. En los últimos años, se ha registrado un preocupante aumento en las tasas de obesidad y sobrepeso entre los adultos peruanos. En 2023, el 26,3 % de la población urbana sufría de obesidad, mientras que, en las áreas rurales, este porcentaje alcanzaba el 14 %. En cuanto al sobrepeso, afectaba al 38,2 % de los residentes urbanos y al 32,9 % de los rurales. Se estima que, para el año 2035, aproximadamente el 35 % de los adultos peruanos padecerán obesidad. A nivel global, se prevé que más de la mitad de la población mundial se verá afectada por el sobrepeso y la obesidad para ese mismo año. Estas alarmantes tendencias representan un desafío creciente de salud pública, con graves implicaciones en enfermedades cardiovasculares y diabetes, lo que requiere una acción integral y políticas basadas en evidencia científica para promover hábitos más saludables y prevenir enfermedades relacionadas con el sobrepeso y la obesidad.
El sobrepeso y la obesidad se definen como una acumulación anormal o excesiva de grasa que puede ser perjudicial para la salud de las personas. Ambas circunstancias se asocian directamente a la mayor probabilidad de sufrir de enfermedades crónicas, como hipertensión arterial, males cardíacos, diabetes y ciertos tipos de cáncer. Para su medición se emplea el índice de masa corporal (IMC), que es una relación entre el peso y la talla de un individuo. En el caso de los adultos, los considerados obesos son aquellas personas que tienen igual o superan los 30kg/m2, mientras que aquellos que tienen un IMC igual o superior a 25 kg/m2 son considerados con sobrepeso. Para el caso de niños y adolescentes, se considera también al IMC, pero ajustado a la edad por la desviación estándar de los patrones de crecimiento infantil; es por ello que se diferencia el grado de sobrepeso y obesidad en niños menores de 5 años y en los niños y adolescentes entre 5 a 19 años [1].
Un elevado índice de masa corporal (IMC) representa un importante factor de riesgo para enfermedades no transmisibles, que incluyen enfermedades cardiovasculares, diabetes, trastornos del sistema locomotor y diversos tipos de cáncer. El riesgo de padecer estas afecciones aumenta a medida que el IMC se incrementa. Además, la obesidad en la niñez se vincula con un mayor riesgo de obesidad en la edad adulta, así como con un aumento en la probabilidad de mortalidad prematura y discapacidades. Los niños con obesidad enfrentan complicaciones que incluyen problemas respiratorios, un mayor riesgo de fracturas, hipertensión y muestran signos tempranos de enfermedades cardiovasculares, resistencia a la insulina, además de efectos adversos en la salud mental. Es crucial abordar esta preocupante tendencia para prevenir futuros problemas de salud y mejorar la calidad de vida de la población [2].
La obesidad en la población peruana de 15 años o más ha mostrado una tendencia creciente, especialmente durante el periodo 2017-2021. Si bien en los últimos años se ha registrado un leve descenso, esta problemática de salud pública ha persistido con el tiempo. A nivel nacional, el porcentaje de obesidad se incrementó de 21 % en 2017 a 24,1 % en 2023, es decir, un aumento de 4,6 puntos porcentuales. Como se aprecia en la Figura 1, en el año 2017, la obesidad en el área urbana representó el 23,6 % de las personas de 15 y más años; mientras que, en el año 2023, la obesidad urbana se elevó a 26,3 %. En el área rural, la incidencia de obesidad también se incrementó, pasando de 11 % en 2017 a 14 % en 2023; sin embargo, la obesidad se mantiene en niveles menores en el área rural comparado con el área urbana a lo largo de todo el periodo [3].
 
Figura 1. Perú: personas de 15 y más años con obesidad en el periodo 2017-2023, por área de residencia (%)
Nota técnica. Excluye a mujeres gestantes.  Nota. Elaboración Ceplan a partir de la base de datos de la ENDES del INEI.
El sobrepeso también mostró una ligera tendencia creciente durante el periodo 2017-2023, elevándose en 1,1 puntos porcentuales, de 36,1 % en el 2017 a 37,2 % en el 2023. Respecto al ámbito de residencia, las áreas rurales experimentaron un aumento significativo del sobrepeso en comparación con las áreas urbanas, aunque mantuvieron índices más bajos. Por ejemplo, en las zonas urbanas, los porcentajes se mantuvieron estables en torno al 38 % (38,6 % en 2017 y 38,2 % en 2023). Por otro lado, en las áreas rurales, el sobrepeso se elevó del 28,6 % al 32,9 % durante el mismo periodo [3].
 
Figura 2. Perú: personas de 15 y más años con sobrepeso en el periodo 2017-2023, por área de residencia (%)
Nota técnica. Excluye a mujeres gestantes. 
Nota. Elaboración Ceplan a partir de la base de datos de la ENDES del INEI (2024).
Al realizar un análisis por dominio de residencia, se observa que la mayor incidencia de sobrepeso y obesidad se presenta en la costa y en Lima metropolitana (Figura 2). En el caso de la obesidad, en la costa se experimentó un incremento de 2,2 puntos porcentuales, pasando de 25,3 % en el año 2017 a 27,5 % en el año 2023; mientras que, en Lima metropolitana, el incremento fue de 1,5 puntos porcentuales, pasando de 26,0 % en 2017 a 27,5 % en el 2023. Con respecto al sobrepeso, tanto en la costa como en Lima Metropolitana, se reportó una ligera diminución, pero aún con una alta incidencia. 
En la costa, hubo una leve reducción de 0,8 puntos porcentuales, es decir, la incidencia de sobrepeso pasó de 38,8 % en 2017 a 38,0 % en 2023; y en Lima Metropolitana, la reducción fue de 1,5 puntos porcentuales, pasando de 39,6 % en 2017 a 38,1 % en 2023. Si bien en la sierra y en la selva la prevalencia de sobrepeso y obesidad es menor que en la costa, en los últimos años se registró un incremento en la incidencia de ambos problemas de salud. 
En la sierra, la obesidad pasó de 12,8 % a 17,3 %, creciendo en 4,5 puntos porcentuales en los años respectivos, convirtiéndose en la región que presentó mayor crecimiento; y en sobrepeso, pasó de 32,4 % en 2017 a 36,4 % en 2023 (+4 p.p.). En cuanto a la región selva, se puede observar que el porcentaje de personas obesas se incrementó de 16,8 % a 20,0 %, es decir, un incremento de 3,2 puntos porcentuales; mientras que, en el sobrepeso incrementó en 2,2 puntos porcentuales al pasar de 32,9 % en 2017 a 34,7 % en 2023 [3].

 
Figura 3. Perú: porcentaje de personas de 15 y más años con obesidad y sobrepeso en el año 2017 y 2023, según dominio de residencia. 
Nota. 1/ Comprende la provincia de Lima y la Provincia Constitucional del Callao. (*) Sólo se cuenta con información desde el segundo semestre del año 2013. Elaboración Ceplan a partir de la base de datos de la ENDES del INEI.

Por otro lado, la obesidad y el sobrepeso afectan tanto a hombres como a mujeres, siendo la obesidad más prevalente en las mujeres. En el periodo 2017-2023, se presenta una tendencia creciente para ambos sexos. En 2017, las mujeres obesas representaron el 24,7 %, mientras que en el 2023, pasaron a ser 28 % (+3,7 p.p.); mientras que, los varones obesos se elevaron de 17,2 % en el año 2017 a 19,9 % en 2023 (+2,7 p.p.). 
 
Figura 4. Perú: porcentaje de personas de 15 y más años con obesidad y sobrepeso en el periodo 2017-2023, por sexo.
Nota. (*) Sólo se cuenta con información desde el segundo semestre del año 2013. No se incluye a mujeres gestantes. Elaboración Ceplan a partir de la base de datos de la ENDES del INEI.
En el caso del sobrepeso, la tendencia es fluctuante tanto para hombres como para mujeres. Para los hombres, la tendencia ascendente comprende el periodo de 2017-2020, de 36,5 % a 39,9 % en 2020, lo que significa un crecimiento de 3,4 puntos porcentuales; no obstante, para el 2023 la tendencia es descendente hasta llegar al 38% (-1,9 p.p.). Para las mujeres, el porcentaje de obesidad cayó de 37,1 % en 2018 a 35,6 % en 2021, evidenciando una caída de 1,5 puntos porcentuales. para posteriormente incrementarse a 36,5 % en el año 2023. 
Al considerar los niveles de bienestar o calidad de vida, se evidencia que la mayor prevalencia de obesidad y sobrepeso se presenta en los quintiles superiores, según los datos del INEI [3]. En el año 2017, el 39,2 % de las personas pertenecientes al nivel de bienestar más alto (Q3 al Q5) registraron sobrepeso, en comparación con el 30,9 % de los pertenecientes al nivel de bienestar más bajo, lo que representa una brecha de 8,3 puntos porcentuales. Esta brecha persiste en 2023, aunque se ha reducido a 3 puntos porcentuales. 
Los índices de obesidad muestran un comportamiento similar. En 2023, los quintiles superiores de bienestar (Q3-Q5) registraron un 27,0 % de obesidad, mientras que, en los quintiles de bienestar más bajo, este porcentaje fue del 19,2 %, lo que significa una brecha de 7,8 puntos porcentuales. En suma, es oportuno resaltar la tendencia que demuestra que las personas con mayor nivel de bienestar o calidad de vida están más expuestas al sobrepeso y la obesidad en comparación con aquellas de menor nivel de bienestar  [3].

  

Figura 5. Perú: porcentaje de personas de 15 y más años con obesidad en el periodo 2013-2023, por niveles de bienestar.  
Nota. Elaboración Ceplan a partir de la base de datos de la ENDES del INEI. 

Según la Organización Mundial de la Salud (2021), el sobrepeso y la obesidad a nivel global se originan en un desequilibrio energético, lo cual significa que las calorías ingeridas superan a las calorías gastadas. Este problema ha sido impulsado por un incremento en el consumo de alimentos altos en calorías y ricos en grasas, así como por una disminución en la actividad física debido a la creciente naturaleza sedentaria del trabajo, los cambios en los medios de transporte y la urbanización. Estos cambios en los hábitos están estrechamente vinculados a factores ambientales y sociales relacionados con el desarrollo, así como a la falta de políticas de apoyo en sectores clave como la salud, la agricultura, el transporte, la planificación urbana, el medio ambiente, la industria alimentaria y la educación. Abordar esta problemática requiere de una acción integral en múltiples frentes para promover hábitos más saludables y prevenir enfermedades asociadas al sobrepeso y la obesidad.
A nivel nacional, se estima que, en 2035, habrá un 35 % de adultos obesos, y que el incremento anual en la obesidad en adultos en el periodo 2020-2035 se mantendrá en 2,5 % [4]. A nivel mundial, se estima que, para el año 2035, más de 4 mil millones de personas en todo el mundo estarán afectadas por el sobrepeso y la obesidad, lo que representa un aumento significativo en comparación con los más de 2,6 mil millones en 2020. Esto significa que más del 50 % de la población mundial estará en esta categoría en 2035 [4].
El sobrepeso y la obesidad representan un creciente desafío de salud a nivel mundial, con graves implicaciones en enfermedades cardiovasculares, diabetes y otros problemas de salud. En particular, la obesidad infantil es preocupante, ya que aumenta el riesgo de enfermedades en la edad adulta. La prevención de estas condiciones requiere la promoción de entornos y elecciones saludables tanto a nivel individual como en la sociedad, respaldada por políticas basadas en evidencia científica y la participación de la industria alimentaria. El acceso a opciones alimentarias saludables y la actividad física debe ser una prioridad para abordar este desafío global de salud pública.
Al respecto, la OMS ha creado el Plan de acción mundial para prevenir enfermedades no transmisibles 2013-2020, que busca cumplir los objetivos acordados en la Declaración Política de la ONU sobre enfermedades no transmisibles. Este plan incluye la reducción de la mortalidad prematura por estas enfermedades en un 25 % para 2025, así como la estabilización de las tasas de obesidad a nivel mundial. En 2019, la Asamblea Mundial de la Salud extendió este plan hasta 2030 y desarrolló una Hoja de Ruta de Implementación 2023-2030 para acelerar el progreso en la prevención y control de ENT. Finalmente, dicha Asamblea ha respaldado el informe de la Comisión para poner fin a la obesidad infantil de 2016 y sus recomendaciones, así como un plan de implementación para combatir la obesidad infantil en distintos entornos y etapas del ciclo de vida [2]. 
Al 2022, ningún país ha logrado reducir la obesidad en toda su población ni está en camino de cumplir con los objetivos de la Organización Mundial de la Salud para el 2025. Para abordar este problema, se necesitan esfuerzos decisivos, centrados en las personas e integrados en todas las etapas de la vida. Las estimaciones sugieren que el costo económico de la obesidad superará los 4 billones de dólares en 2035, casi el 3 % del PIB global [4]. 

'''

placeholder_ref= '''
Bibliografía

[1] 	OMS, «Obesidad y sobrepeso,» 14 Setiembre 2022. [En línea]. Available: https://www.who.int/es/news-room/fact-sheets/detail/obesity-and-overweight.
[2] 	OMS, «Obesidad y sobrepeso,» 2021. [En línea]. Available: https://www.who.int/es/news-room/fact-sheets/detail/obesity-and-overweight.
[3] 	INEI, «Perú: Enfermedades no transmisibles y transmisibles, 2023,» 2024. [En línea]. Available: https://www.inei.gob.pe/media/MenuRecursivo/publicaciones_digitales/Est/Lib1839/.
[4] 	WOA, «atlas de la obesidad,» 2023. [En línea]. Available: https://data.worldobesity.org/publications/WOF-Obesity-Atlas-V5.pdf.
[5] 	INEI, «Enfermedades transmitibles y no transmitibles 2022,» 2023. [En línea]. Available: https://cdn.www.gob.pe/uploads/document/file/4570237/Per%C3%BA%3A%20Enfermedades%20No%20Transmisibles%20y%20Transmisibles%2C%202022.pdf?v=1684338910.
'''

# Streamlit UI
st.sidebar.header("Placeholder")
st.sidebar.subheader("Texto de prueba")
st.sidebar.code(placeholder_text)
st.sidebar.subheader("Referencias de prueba")
st.sidebar.code(placeholder_ref)