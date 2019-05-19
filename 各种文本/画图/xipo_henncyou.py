import csv
import os
import numpy as np
import librosa
import librosa.display
import soundfile as sf
import matplotlib.pyplot as plt

os.chdir(r"C:\Users\a7825\Desktop\新建文件夹 (4)")
sr = 16000
nfft = 2048
win = 0.025
hop = 0.1
nmels = 40

mel_specs = []
labels = []


wavfile = r"C:\Users\a7825\Desktop\新建文件夹 (4)\C1_F_01\wav/l_8820_9970_C1_F_01.wav"

wave, _ = librosa.load(wavfile, sr=sr)
wave_data = np.array(wave, dtype=np.float32)

power_spectrogram = np.abs(
    librosa.stft(
        wave_data + np.spacing(1),
        n_fft=nfft,
        hop_length=int(hop * sr),
        win_length=int(win * sr),
        window="hamming",
        center=True
    ))
librosa.display.specshow(librosa.amplitude_to_db(power_spectrogram, ref=np.max), y_axis='log', x_axis='time')
plt.show()
plt.subplot(1, 2, 1)
plt.plot(np.abs(librosa.stft(power_spectrogram[0])))

power_spectrogram = power_spectrogram ** 2
mel_basis = librosa.filters.mel(
    sr=sr,
    n_fft=nfft,
    n_mels=40,
    fmin=0.0,
    fmax=sr / 2.0,
    htk=False,
    norm=1
)

mel_spec = np.dot(mel_basis, power_spectrogram)

print(mel_spec.shape)
plt.subplot(1, 2, 2)
plt.plot(np.abs(librosa.stft(mel_spec[0])))
print(np.abs(librosa.stft(mel_spec[0])).shape)
plt.show()
out = np.log(mel_spec + np.spacing(1))
out = out.T