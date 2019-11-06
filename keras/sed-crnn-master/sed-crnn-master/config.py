is_mono = True  # True: mono-channel input, False: binaural input
sr = 44100
nfft = 2048
frames_1_sec = int(sr/(nfft/2.0))


path_train = r'C:\Users\a7825\Desktop\40_8_8/train.npz'  # 使用真实数据
path_test = r'C:\Users\a7825\Desktop\40_8_8/test.npz'


nb_ch = 1 if is_mono else 2
batch_size = 10            # Decrease this if you want to run on smaller GPU's
fft_point = 8
seq_len = int(fft_point//2)       # Frame sequence length. Input to the CRNN.
nb_epoch = 1            # Training epochs
patience = int(0.25 * nb_epoch)  # Patience for early stopping
gpuzhiding = False#是否指定gpu
visible_device_list="1"

# Number of frames in 1 second, required to calculate F and ER for 1 sec segments.
# Make sure the nfft and sr are the same as in feature.py

cnn_nb_filt = 32            # CNN filter size
kernel_size=(3, 3)
cnn_pool_size = [2, 2, 2]   # Maxpooling across frequency. Length of cnn_pool_size =  number of CNN layers
rnn_nb = [32, 32]           # Number of RNN nodes.  Length of rnn_nb =  number of RNN layers                        # rnn的层数等于rnn_nb的长度
fc_nb = 2                # Number of FC nodes.  Length of fc_nb =  number of FC layers
dropout_rate = 0.0          # Dropout after each layer
lr = 0.0001

