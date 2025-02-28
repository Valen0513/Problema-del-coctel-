# Problema-del-coctel-
1. Introducción

En entornos ruidosos donde varias personas hablan simultáneamente, como en un evento tipo cóctel, la captación de una sola voz puede representar un desafío. Este fenómeno, conocido como el "problema de la fiesta de cóctel", es un problema clásico en procesamiento de señales y tiene aplicaciones en reconocimiento de voz, audición artificial y mejora de la calidad del audio. En este laboratorio, se implementó un sistema de separación de fuentes mediante el método de Análisis de Componentes Independientes (ICA) para extraer la voz de un participante específico.

2. Configuración del Sistema

La configuración del sistema se diseñó con base en criterios rigurosos para garantizar una captura óptima de las señales y una correcta aplicación del algoritmo ICA. Se utilizó un arreglo de dos celulares de los cuales se desacargaron aplicaciones de audio para grabar, colocados estratégicamente en la sala para capturar las mezclas de las voces de los hablantes.

2.1 Ubicación y Distancias

Los micrófonos y las fuentes sonoras se ubicaron de la siguiente manera:

Hablante 1 a celular 1: 0.72 m
Hablante 2 a celular 2: 0.87 m
Hablante 1 a celular 2: 0.90
Hablante 2 a celular 1: 0.78
Hablante 1 a hablante 2: 0.65 
celular 1 a celular 2: 1.46
Distancia entre micrófonos: 1.0 m
Velocidad del sonido en aire: 343 m/s

Estos valores permitieron calcular los retardos en la llegada de las señales a cada micrófono, un aspecto clave para la aplicación del algoritmo ICA.

2.2 Orientación de las Fuentes y Micrófonos

Los micrófonos se distribuyeron de manera que cada uno captara diferentes combinaciones de las voces. Las personas se ubicaron en posiciones fijas con direcciones distintas, lo que generó una superposición natural de las señales en cada micrófono. Esta configuración permitió recrear un escenario realista del problema de la fiesta de cóctel.
