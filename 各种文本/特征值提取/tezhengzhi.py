import wavio
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
path =r"C:\Users\a7825\Desktop\新しいフォルダー/a.wav"

wav_struct=wavio.read(path)
wav=wav_struct.data.astype(float)/np.power(2,wav_struct.sampwidth*8-1)
f,t,X=signal.spectral.spectrogram(wav,np.hamming(1024),nperseg=1024,noverlap=0,detrend=False,return_onesided=True,mode='magnitude')
print(X)
plt.pcolormesh(t, f, X)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()