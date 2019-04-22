# coding=utf-8
#西坡呢変調スペクトル
import os

import librosa
import librosa.display
import numpy as np

import commons.config as cfg



class Extractor:
    def __init__(self):
        self.sampling_rate = 0
        self.nfft = 0
        self.win = 0
        self.hop = 0

    def extract(self, *args):
        return NotImplementedError


class ModulationSpectrum(Extractor):
    def __init__(
            self, sampling_rate=16000, num_fft=2048, n_mels=40, win=0.025, hop=0.01, frame_length=32
    ):
        super(ModulationSpectrum, self).__init__()
        self.sampling_rate = sampling_rate
        self.nfft = num_fft
        self.nmels = n_mels
        self.win = int(win * sampling_rate)
        self.hop = int(hop * sampling_rate)
        self.frame_length = frame_length

    def extract(self, wavfile):
        dir = r'C:\Users\a7825\Desktop\工作空间\杂物\临时\这个就对了/这个就对了.csv'
        modspecs = []
        wave, _ = librosa.load(dir + wavfile, sr=self.sampling_rate)
        wave_data = np.array(wave, dtype=np.float32)

        wave_data = wave_data.astype(np.double)

        stft = np.abs(
            librosa.stft(
                wave_data + np.spacing(1),
                n_fft=self.nfft,
                hop_length=self.hop,
                win_length=self.win,
                window='hamming',
                center=True
            ))
        power_spectrogram = stft ** 2

        mel_basis = librosa.filters.mel(
            sr=self.sampling_rate,
            n_fft=self.nfft,
            n_mels=self.nmels,
            fmin=0.0,
            fmax=self.sampling_rate / 2.0,
            htk=False,
            norm=1
        )
        mel_spec = np.dot(mel_basis, power_spectrogram)

        #np.savetxt(cfg.blstm_filterbank_dir + wavfile + '.csv', mel_spec.T, delimiter=',')
        modspec = []
        for filterbank in mel_spec:
            ms = []
            X =np.abs(
                librosa.stft(
                    filterbank + np.spacing(1),
                    n_fft=self.frame_length,
                    hop_length=1,
                    window='hamming',
                    center=True
                ))
            modspec.extend(X)
        modspec = np.array(modspec).T
        np.savetxt(cfg.blstm_iiyodomi_dir + wavfile + '.csv', modspec, delimiter=',')
        modspecs.append(modspec)
        return modspec


if __name__ == '__main__':
    dir = cfg.source_iiyodomi_dir
    os.chdir(dir)

    mod_spec = ModulationSpectrum()
    """

    try:
        os.stat(cfg.blstm_modspec_dir)
    except:
        os.mkdir(cfg.blstm_modspec_dir)

    try:
        os.stat(cfg.blstm_filterbank_dir)
    except:
        os.mkdir(cfg.blstm_filterbank_dir)
"""

    try:
        os.stat(cfg.blstm_iiyodomi_dir)
    except:
        os.mkdir(cfg.blstm_iiyodomi_dir)

    gender = os.listdir(dir)
    for g in gender:
        washa = os.listdir(dir + g)
        """

        try:
            os.stat(cfg.blstm_modspec_dir + g + '/')
        except:
            os.mkdir(cfg.blstm_modspec_dir + g + '/')

        try:
            os.stat(cfg.blstm_filterbank_dir + g + '/')
        except:
            os.mkdir(cfg.blstm_filterbank_dir + g + '/')
"""

        try:
            os.stat(cfg.blstm_iiyodomi_dir + g + '/')
        except:
            os.mkdir(cfg.blstm_iiyodomi_dir + g + '/')

        for w in washa:
            """

            try:
                os.stat(cfg.blstm_filterbank_dir + g + '/'+ w + '/')
            except:
                os.mkdir(cfg.blstm_filterbank_dir + g + '/'+ w + '/')

            try:
                os.stat(cfg.blstm_iiyodomi_dir + g + '/' + w + '/')
            except:
                os.mkdir(cfg.blstm_iiyodomi_dir + g + '/' + w + '/')
"""
            try:
                os.stat(cfg.blstm_iiyodomi_dir + g + '/' + w + '/')
            except:
                os.mkdir(cfg.blstm_iiyodomi_dir + g + '/' + w + '/')
                
            # modulation_spectrum
            files = os.listdir(dir + g + '/' + w)
            for f in files:
                ms = mod_spec.extract(g + '/' + w + '/' + f)
        """
        with open(cfg.blstm_modspec_dir + g + '/' + 'speakers.txt', 'w') as f:
            for w in washa:
                f.write("%s\n" % w)

        with open(cfg.blstm_filterbank_dir + g + '/' + 'speakers.txt', 'w') as f:
            for w in washa:
                f.write("%s\n" % w)
        """
        with open(cfg.blstm_iiyodomi_dir + g + '/' + 'speakers.txt', 'w') as f:
            for w in washa:
                f.write("%s\n" % w)
