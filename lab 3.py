
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA
import soundfile as sf


audio1,sr=librosa.load("audio 1lina.wav",sr=None)
audio2,sr=librosa.load("audio2valen.wav",sr=None)
audio3,sr=librosa.load("audioambiente1.wav",sr=None)

muestras_2min = 2 * 60 * sr  
audio1_inicio = audio1[:muestras_2min]  
audio2_inicio = audio2[:muestras_2min]
audio3_inicio = audio3[:muestras_2min]

potencia_señal1=np.mean(audio1_inicio**2)
potencia_señal2=np.mean(audio2_inicio**2)
potencia_señal3=np.mean(audio3_inicio**2)

SNR1=10*np.log10(potencia_señal1/potencia_señal3)
SNR2=10*np.log10(potencia_señal2/potencia_señal3)

print ("el SNR del audio 1 es: ",SNR1,"dB")
print ("el SNR del audio 2 es: ",SNR2,"dB")

dist_h1_m1 = 0.72  
dist_h2_m2 = 0.87  
dist_h1_m2 = 0.90 
dist_h2_m1 = 0.78 
dist_m1_m2 = 1.46  
vel_sonido = 343  


retardo_h1_m1 = int((dist_h1_m1 / vel_sonido) * sr)
retardo_h2_m2 = int((dist_h2_m2 / vel_sonido) * sr)
retardo_h1_m2 = int((dist_h1_m2 / vel_sonido) * sr)
retardo_h2_m1 = int((dist_h2_m1 / vel_sonido) * sr)


audio1 = np.pad(audio1, (retardo_h1_m1, 0))[:len(audio1)]
audio2 = np.pad(audio2, (retardo_h2_m2, 0))[:len(audio2)]


audio1 *= 1 / (dist_h1_m1 ** 2 + dist_h1_m2 ** 2)
audio2 *= 1 / (dist_h2_m2 ** 2 + dist_h2_m1 ** 2)

total_muestras = min(len(audio1), len(audio2))


plt.figure(figsize=(10, 4))
librosa.display.waveshow(audio1, sr=sr, alpha=0.5, color="green", label="Audio 1")
librosa.display.waveshow(audio2, sr=sr, color="pink", alpha=0.5, label="Audio 2")

plt.legend()
plt.title("Señales capturadas por los micrófonos")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()

frecuencia=np.fft.fftfreq(len(audio1), 1/sr)
trans_audio1=np.fft.fft(audio1)
trans_audio2=np.fft.fft(audio2)

pastel_blue = (0.6, 0.8, 1)
plt.figure(figsize=(10, 4))
plt.plot(frecuencia[:len(frecuencia)//2], np.abs(trans_audio1[:len(frecuencia)//2]), color="purple", label="Audio 1")
plt.plot(frecuencia[:len(frecuencia)//2], np.abs(trans_audio2[:len(frecuencia)//2]), color=pastel_blue, label="Audio 2")

plt.legend()
plt.title("Espectro de Frecuencia (FFT)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.show()

plt.figure(figsize=(10, 4))
plt.semilogy(frecuencia[:len(frecuencia)//2], np.abs(trans_audio1[:len(frecuencia)//2]), color="purple", label="Audio 1")
plt.semilogy(frecuencia[:len(frecuencia)//2], np.abs(trans_audio2[:len(frecuencia)//2]), color=pastel_blue, label="Audio 2")
plt.legend()
plt.title("Espectro de Frecuencia (FFT)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.show()

total_muestras = min(len(audio1_inicio), len(audio2_inicio))
F = np.array([audio1[:total_muestras], audio2[:total_muestras]]).T

ica = FastICA(n_components=2, random_state=42)
señales_separadas = ica.fit_transform(F)

energias = [np.mean(señal**2) for señal in señales_separadas.T]
indice_voz = np.argmax(energias)  

voz_extraida = señales_separadas[:, indice_voz]

potencia_voz = np.mean(voz_extraida**2)
potencia_ruido = np.mean(audio3[:total_muestras]**2)

snr_voz = 10 * np.log10(potencia_voz / potencia_ruido)

voz_extraida /= np.max(np.abs(voz_extraida))

sf.write("voz_extraida.wav", voz_extraida, sr)

plt.figure(figsize=(10, 4))
librosa.display.waveshow(voz_extraida, sr=sr, color="blue")
plt.title("Señal de Voz Extraída (La Más Fuerte)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.show()


frecuencia = np.fft.fftfreq(len(voz_extraida), 1/sr)
transformada = np.fft.fft(voz_extraida)

plt.figure(figsize=(10, 4))
plt.plot(frecuencia[:len(frecuencia)//2], np.abs(transformada[:len(frecuencia)//2]), color="purple")
plt.title("Espectro de Frecuencia de la Voz Extraída")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.show()

plt.figure(figsize=(10, 4))
plt.semilogy (frecuencia[:len(frecuencia)//2], np.abs(transformada[:len(frecuencia)//2]), color="purple")
plt.title("Espectro de Frecuencia de la Voz Extraída")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.show()

print(f"La voz extraída corresponde a la fuente {indice_voz + 1}.")
print(f"SNR de la voz extraída: {snr_voz:.2f} dB")
print("La señal ha sido guardada como 'voz_extraida.wav'.")
