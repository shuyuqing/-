import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav


basedir = r'C:\Users\a7825\Desktop\工作空间\セミナー\语音\wav/C001L_007.wav'

(fs, audio) = wav.read(basedir)

wave_data = np.array(audio, dtype=np.float32)


Xdata = np.linspace(0, len(wave_data), len(wave_data), endpoint=False)
# print(Xdata)
# plt.plot(Xdata, wave_data)
# plt.show()


# plt.subplot(1, 2, 1)
# plt.plot(wave_data)
# plt.show()


fig = plt.figure()

