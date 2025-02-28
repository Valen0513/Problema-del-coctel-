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

- Luego a una variable se le asigna el nombre del archivo que ya esta en wav, donde sr es la frecuencia de muestreo, que corresponde a 44,1 khz, los niveles de cuantificación son de 16 bits por muestra.
   
 ![image](https://github.com/user-attachments/assets/8e73e659-02d2-47f5-bdab-e11f43c63b15)

- Se calcula cuántas muestras corresponden a los primeros 2 minutos de la grabación, se extraen los primeros 2 minutos de cada audio para analizar solo esa parte de la señal, para luego calcular su SNR de ambos audios se utiliza la seiguiente formula:

![Captura de pantalla 2025-02-28 162453](https://github.com/user-attachments/assets/5f26792f-00fc-4089-bc47-08d6a0176fd4)

Donde: Pseñal es la potencia de la voz capturada por cada audio, y Pruido es la potencia de la grabacion del ambiente 

Se calcula la potencia promedio de cada señal, que es el promedio de los valores al cuadrado (una medida de la energía de la señal).

![Captura de pantalla 2025-02-28 161837](https://github.com/user-attachments/assets/842625cc-4b5b-4c26-956f-9c22f4929693)

Utilizando la formula anteriormente mencionada se calcula el SNR de cada audio con respecto al audio del ambiente en dB 

Los resultados fueron: el SNR del audio 1 es:  19.52798366546631 dB, el SNR del audio 2 es:  24.88265037536621 dB

- Se establecieron las distancias en metros entre los hablantes y los celulares, cada señal de audio tiene un retardo en función de la distancia que el sonido debe recorrer desde el hablante hasta el celular. Se calcula con la fórmula: tiempo retardado igual a la distancia sobre la velocidad del sonido, este tiempo se convierte en número de muestras multiplicándolo por la frecuencia de muestreo (sr), usando la funcion np.pad() que agrega ceros al inicio de la señal simulando el tiempo de propagación del sonido antes de ser captado por el micrófono. Se calcula un factor de atenuación para cada señal basado en la distancia de los hablantes a los celulares, se obtiene la cantidad mínima de muestras entre las señales para asegurar que tengan la misma longitud antes de graficarlas. Luego se grafica utilizando la biblioteca import matplotlib.pyplot as plt para graficar y la biblioteca import librosa.display para que muestre la forma de la onda que da cada audio, se le asigna un color a cada señal, un tamaño al grafico y se le añaden etiquetas y leyenda para identificar las señales. 

![image](https://github.com/user-attachments/assets/e55c31c9-720b-4de9-b75d-0da92b11e72b)

La representacion grafica de las señales de ambos audios es: 

![image](https://github.com/user-attachments/assets/0036298c-dc5f-48fd-aa6a-07ebff4db578)

- Se calcula la transfromada de Fourier rapida y su grafica para pasar del dominio del tiempo al dominio de la frecuencia, se calcula la frecuencia con las funciones para la transformada, se aplica la transformada a cada audio. Se grafican las magnitudes de la FFT  en función de las frecuencias, Solo se usa la mitad del espectro porque la FFT es simétrica respecto al eje de Nyquist. Se le da un tamaño al grafico, un nombre a cada eje y una leyenda para identificar.

![image](https://github.com/user-attachments/assets/3b235c17-3e98-4c42-915e-ac96a482d385)

El espectro de la transfromada de Fourier es: 

![image](https://github.com/user-attachments/assets/04822bf2-db45-4e26-b65d-916249580f57)

El espectro de la transformada de Fourier en escala logaritmica es:

![image](https://github.com/user-attachments/assets/691a4178-d9bc-494c-b562-a739e95a07dd)

- Se aplicó el método ICA para separar las fuentes independientes. Se crea una matriz F que contiene la señal captada por cada audio, la T al final representa que Transpone la matriz para que las filas representen muestras en el tiempo y las columnas representen los audios. Se aplica ICA con dos componentes porque tiene dos señales mezcladas, fit_transform(F): Ajusta el modelo a los datos y devuelve las señales separadas en la variable señales_separadas, esta variable contiene las dos señales separadas una en cada columna. Se calcula la energia de la señal separada que representa el promedio de la potencia, la variable indice _voz tiene el indice de la señal con mayor energia lo que supone que es la voz mas fuerte. La variable voz_extraida extrae la señal de la voz que tiene mayor energia calculada en la anterior variable. Se calcula la potencia promedio de la voz extraida para calcular su SNR que es la potencia_voz sobre la potencia_rudido y se le aplica log para que sea en dB.

![image](https://github.com/user-attachments/assets/06c504d3-4084-4ffc-a51b-03e2bad1f919)

Los resultados son: La voz extraída corresponde a la fuente 2, SNR de la voz extraída: 64.16 dB, La señal ha sido guardada como 'voz_extraida.wav'.

- Se normaliza la señal dividiendo por su valor absoluto máximo, asegurando que la amplitud máxima esté en ±1 para evitar distorsiones al guardarla en un archivo, sf.write de la libreria import soundfile as sf Guarda la señal extraída como un archivo de audio (voz_extraida.wav) con la frecuencia de muestreo sr. Luego se grafica la señal de la voz extraida, librosa.display.waveshow muestra la forma de onda de la señal de voz extraída, se agrega un titulo a cada eje, se dibuja el grafico.

![image](https://github.com/user-attachments/assets/1996278f-c21e-46fb-96f9-66f61ce34463)

La grafica de la señal extraida es: 

![image](https://github.com/user-attachments/assets/db80f1fb-b902-4c1c-b031-049dadace1e2)

- Por ultimo se calcula la transformada de Fourier y el espectro de la señal extraida. Se calculan los valores de la frecuencia para la transformada con el numero total de muestras de la voz extraida y con su periodo de muestreo, se calcula la transfromada de Fourier rapida contiene los coeficientes de frecuencia donde la magnitud representa la amplitud de cada freceucnia y la fase que indica el desfase en una determinada frecuencia 


Se seleccionó la señal correspondiente a la voz de interés, evaluando su relación señal a ruido (SNR).
