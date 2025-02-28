# Problema-del-coctel-
1. Introducción

En entornos ruidosos donde varias personas hablan simultáneamente, como en un evento tipo cóctel, la captación de una sola voz puede representar un desafío. Este fenómeno, conocido como el "problema de la fiesta de cóctel", es un problema clásico en procesamiento de señales y tiene aplicaciones en reconocimiento de voz, audición artificial y mejora de la calidad del audio. En este laboratorio, se implementó un sistema de separación de fuentes mediante el método de Análisis de Componentes Independientes (ICA) para extraer la voz de un participante específico.

2. Configuración del Sistema

La configuración del sistema se diseñó con base en criterios rigurosos para garantizar una captura óptima de las señales y una correcta aplicación del algoritmo ICA. Se utilizó un arreglo de dos celulares de los cuales se desacargaron aplicaciones de audio para grabar, colocados estratégicamente en la sala para capturar las mezclas de las voces de los hablantes.

2.1 Ubicación y Distancias

Los micrófonos y las fuentes sonoras se ubicaron de la siguiente manera:

Hablante 1 a celular 1: 0.72 m

Hablante 2 a celular 2: 0.87 m

Hablante 1 a celular 2: 0.90 m

Hablante 2 a celular 1: 0.78 m

Hablante 1 a hablante 2: 0.65 m

celular 1 a celular 2: 1.46 m

Distancia entre micrófonos: 1.0 m

Velocidad del sonido en aire: 343 m/s

Estos valores permitieron calcular los retardos en la llegada de las señales a cada micrófono, un aspecto clave para la aplicación del algoritmo ICA.

2.2 Orientación de las Fuentes y Micrófonos

Los micrófonos se distribuyeron de manera que cada uno captara diferentes combinaciones de las voces. Las personas se ubicaron en posiciones fijas con direcciones distintas, lo que generó una superposición natural de las señales en cada micrófono. Esta configuración permitió recrear un escenario realista del problema de la fiesta de cóctel.

3. Metodología

Se conectaron tres micrófonos a un sistema de adquisición de datos y se ubicaron de acuerdo con la distribución mencionada.

Se grabaron las señales de audio mientras los hablantes conversaban simultáneamente.

Se preprocesaron las señales, eliminando posibles ruidos no deseados y normalizando su amplitud.
- Primero se convierten los audios que estan en unknown a archivos wav para que sean leidos por la libreria librosa en python 
- Se importaron estas bibliotecas para que leyeran el audio
  
![image](https://github.com/user-attachments/assets/39f3659c-db98-497c-b565-29e006f635ba)

- Luego a una variable se le asigna el nombre del archivo que ya esta en wav, donde sr es la frecuencia de muestreo, que corresponde a 44,1 khz
   
 ![image](https://github.com/user-attachments/assets/8e73e659-02d2-47f5-bdab-e11f43c63b15)

- Se calcula cuántas muestras corresponden a los primeros 2 minutos de la grabación, se extraen los primeros 2 minutos de cada audio para analizar solo esa parte de la señal, para luego calcular su SNR de ambos audios se utiliza la seiguiente formula:

![Captura de pantalla 2025-02-28 162453](https://github.com/user-attachments/assets/5f26792f-00fc-4089-bc47-08d6a0176fd4)

Donde: Pseñal es la potencia de la voz capturada por cada audio, y Pruido es la potencia de la grabacion del ambiente 

![Captura de pantalla 2025-02-28 161837](https://github.com/user-attachments/assets/842625cc-4b5b-4c26-956f-9c22f4929693)


Se aplicó el método ICA para separar las fuentes independientes.

Se seleccionó la señal correspondiente a la voz de interés, evaluando su relación señal a ruido (SNR).
