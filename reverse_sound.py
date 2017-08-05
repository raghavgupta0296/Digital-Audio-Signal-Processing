import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

fs, data = wav.read("nom.wav")
# print(f)
# plt.plot(data)
# plt.show()
data = data[::-1]
wav.write("reverse_nom.wav",fs,data)