'''
SUMMARY:  Extract features, copy from acoustic_classification_2013
AUTHOR:   Qiuqiang Kong
Created:  2016.05.23
Modified: 2016.06.25
          2016.10.11 Modify variable name
--------------------------------------
'''

from chainer import Variable
import csv
import sys
sys.path.append('activity_detection')
import numpy as np
from scipy import signal
import wavio
import config as cfg
import os
import matplotlib.pyplot as plt
import pickle as cPickle
import librosa
from scipy import io
from hat.preprocessing import pad_trunc_seq
from activity_detection import activity_detection






########### FOR DCASE MODEL #############

'''
label_dif = np.array([["clearthroat",1],
             ["cough", 2],
             ["pageturn", 3],
             ["speech", 4],
             ["keys", 5],
             ["laughter", 6],
             ["keyboard", 7],
             ["drawer", 8],
             ["phone", 9],
             ["doorslam", 10],
             ["knock", 11]])
'''

label_dif = np.array([

["clearthroat",1],
             ["phone", 2],
             ["pageturn", 3],
             ["speech", 4],
             ["keys", 5],
             ["laughter", 6],
             ["keyboard", 7],
             ["drawer", 8],
             ["cough", 9],
             ["doorslam", 10],
             ["knock", 11]])


### readwav
def readwav( path ):
    Struct = wavio.read( path )
    wav = Struct.data.astype(float) / np.power(2, Struct.sampwidth*8-1)
    fs = Struct.rate
    return wav, fs

# calculate mel feature
def GetMel( wav_fd, fe_fd, n_delete ):
    names = [ na for na in os.listdir(wav_fd) if na.endswith('.wav') ]
    names = sorted(names)
    for na in names:
        print(na)
        path = wav_fd + '/' + na
        wav, fs = readwav( path )
        if ( wav.ndim==2 ): 
            wav = np.mean( wav, axis=-1 )
        assert fs==cfg.fs
        ham_win = np.hamming(cfg.win)
        [f, t, X] = signal.spectral.spectrogram( wav, window=ham_win, nperseg=cfg.win, noverlap=662, detrend=False, return_onesided=True, mode='magnitude' ) 
        X = X.T
        
        # define global melW, avoid init melW every time, to speed up. 
        if globals().get('melW') is None:
            global melW
            melW = librosa.filters.mel( fs, n_fft=cfg.win, n_mels=40, fmin=0., fmax=22100 )
            print(melW)
            melW /= np.max(melW, axis=-1)[:,None]
            
        X = np.dot( X, melW.T )
        X = X[:, n_delete:]
        #print(X.shape)
        # DEBUG. print mel-spectrogram
        #plt.matshow(np.log(X.T), origin='lower', aspect='auto')
        #plt.show()
        #pause
        
        out_path = fe_fd + '/' + na[0:-4] + '.f'
        cPickle.dump( X, open(out_path, 'wb'), protocol=cPickle.HIGHEST_PROTOCOL )


def TransMulti(label0):
    #print("-----------TRNAS------------")
    #print(label0)
    labelm = []

    for i in range(len(label0)):
        label = np.array( [[0 for t in range(11)] for k in range(len(label0[i]))] )
        #label = [[0 for t in range(11)] for k in range(len(label0[i]))] 
        label = label.astype(np.int32)
        #print(label[0])
        for j in range(11):
            if label0[i][0] == j:
               for k in range(len(label0[i])):
                   label[k][j] = 1
            #labeln = Variable(np.array(label))
        #print(label.shape)        
        labelm.append(label)
    
    return labelm






          
###
# return X: (n_sample,max_len,n_freq), y: (n_sample)
def GetAllData( fe_fd, max_len ):
    names = os.listdir( fe_fd )
    names = sorted(names)
    #print(names)
    Xall, yall = [], []
    #print(len(names))
    num = 0
    for na in names:
        if na == 'clearthroat002.f':
            # load data
            num = num + 1
            path = fe_fd + '/' + na
            lb = na[0:-5]
            #print("lb")
            #print(lb)
            X = cPickle.load( open(path, 'rb') )
            #print("print X")
            #print(X.shape)
            #print(na)
            #print("print X")
            #print(len(X[:,0]))
    
            # pad or trunc data
            #X = pad_trunc_seq( X, max_len )  #default is ack
            #print("-----------------")
            #print(len(X[:,0]))
            y = cfg.lb_to_id[lb]

            #Y = np.array([[0 for i in range(11)] for j in range( len(X[:,0]) )])
            Y = np.array([y for i in range( len(X[:,0]) )])


            #print(Y.shape)
            #for i range():
            #Y[:,y] = 1;
            Y = Y.astype(np.int32)#if you use BLSTM
            #print(Y)
            Xall.append( X )
            yall.append( Y )
    #print("num = ")
    #print(num)
    Xall = np.array(Xall)
    #yall = np.array(yall)
    #print(yall)
    #print(np.array(yall))
    #return np.array( Xall ), np.array( yall )
    return Xall, yall

###
# read annotation file    
def ReadAnn( txt_file, na):
    ann_path = txt_file + '/' + na
    lists = []

    tr_fe_fd = cfg.dev_tr2_fe_mel_fd
    fr = open( ann_path, 'r') 
    tr_fe = tr_fe_fd + '/' + na[0:-4] + '.f'
    X = cPickle.load( open(tr_fe, 'rb') )
    T = len(X)
    label = np.array( [[0 for t in range(11)] for k in range(len(X))] )
    label = label.astype(np.int32)
    index = 0;

    for line in fr.readlines():
#if BLSTM
        #print(label[10][10])
        line_list = line.split('\t')
        bgn, fin, lb = float(line_list[0]), float(line_list[1]), line_list[2].split('\n')[0]

        for i in range(11):
            if lb == label_dif[i,0]:

                for j in range(int(bgn*100),int(fin*100-1)):
                    label[j][i] = 1
        index += 1   
    return label

def ReadAnn0(na):

    tr_fe_fd = cfg.dev_tr1_fe_mel_fd + '/none'
    tr_fe = tr_fe_fd + '/' + na[0:-4] + '.f'
    X = cPickle.load( open(tr_fe, 'rb') )
    T = len(X)
    label = np.array( [[1 for t in range(11)] for k in range(len(X))] )
    #for i in range(len(X)):
    #    label[i][0] = 1 
    label = label.astype(np.int32)
  
    return label






def ReadAnn1( txt_file, na, e_label):
    ann_path = txt_file + '/' + na
    lists = []

    tr_fe_fd = cfg.dev_fe_fd + '/d_0/' + e_label
    fr = open( ann_path, 'r') 
    tr_fe = tr_fe_fd + '/' + na[0:-4] + '.f'
    X = cPickle.load( open(tr_fe, 'rb') )
    T = len(X)
    label = np.array( [[1 for t in range(11)] for k in range(len(X))] )

    #for i in range(len(X)):
    #    label[i][0] = 1 

    label = label.astype(np.int32)
    index = 0;

    for line in fr.readlines():
#if BLSTM
        #print(label[10][10])
        line_list = line.split('\t')
        bgn, fin, lb = float(line_list[0]), float(line_list[1]), line_list[2].split('\n')[0]

        for i in range(11):
            if lb == label_dif[i,0]:

                for j in range(int(bgn*100),int(fin*100-1)):
                    label[j][i] = 2
 
        index += 1   
    return label






def ReadCTCAnn0(na):

    label = np.array( [[1 for t in range(11)] for k in range(3)] )
    label = label.astype(np.int32)
  
    return label


def ReadCTCAnn1( txt_file, na, e_label):
    ann_path = txt_file + '/' + na
    lists = []

    tr_fe_fd = cfg.dev_fe_fd + '/d_0/' + e_label
    fr = open( ann_path, 'r') 
    tr_fe = tr_fe_fd + '/' + na[0:-4] + '.f'
    X = cPickle.load( open(tr_fe, 'rb') )
    T = len(X)
    label = np.array( [[1 for t in range(11)] for k in range(3)] )# 3 is label seq length
    index = 0;

    for line in fr.readlines():
#if BLSTM
        #print(label[10][10])
        line_list = line.split('\t')
        bgn, fin, lb = float(line_list[0]), float(line_list[1]), line_list[2].split('\n')[0]

        for i in range(11):
            if lb == label_dif[i,0]:
                for j in range(1):
                    #if j > 3 and j < 8:
                        label[1][i] = 2

    label = label.astype(np.int32)  
    return label



###
# get out_list from scores
def OutMatToList( pred ):
    
    lists = []
    '''
    for i in range ( len(pred) ):
        #print(pred[i])
        if pred[i] != 0:
            print("not")
            #print(pred[i])

    for i2 in range( len(bgn_fin_pairs) ): 
        lists.append( { 'event_label':cfg.id_to_lb[i1], 
                        'event_onset':bgn_fin_pairs[i2]['bgn'] / (44100./1024.), 
                        'event_offset':bgn_fin_pairs[i2]['fin'] / (44100./1024.) } )
    
    for i1 in range( n_class ):
        bgn_fin_pairs = activity_detection( scores[:,i1], thres, n_smooth )
        #print(bgn_fin_pairs)

        for i2 in range( len(bgn_fin_pairs) ): 
            lists.append( { 'event_label':cfg.id_to_lb[i1], 
                            'event_onset':bgn_fin_pairs[i2]['bgn'] / (44100./1024.), 
                            'event_offset':bgn_fin_pairs[i2]['fin'] / (44100./1024.) } )
    '''
    return lists

# show f value
def ShowResults( results ):
    F_ary = []
    for r in results:
        F_ary.append( r['overall']['F'] )
    print('mean F value:', np.mean( F_ary ))

def WriteOutToTxt( out_path, out_list ):
    f = open( out_path, 'w' )
    for li in out_list:
        f.write( str(li['event_onset']) + '\t' + str(li['event_offset']) + '\t' + li['event_label'] + '\n')
    f.close()
    print('Write out detections to', out_path, 'successfully!')

###    
# create an empty folder
def CreateFolder( fd ):
    if not os.path.exists(fd):
        os.makedirs(fd)
        
if __name__ == "__main__":
    CreateFolder( cfg.dev_fe_fd )
    CreateFolder( cfg.dev_tr_fe_mel_fd )
    CreateFolder( cfg.dev_te_fe_mel_fd )
    
    GetMel( cfg.dev_tr_wav_fd, cfg.dev_tr_fe_mel_fd, n_delete=1 )
    GetMel( cfg.dev_te_wav_fd, cfg.dev_te_fe_mel_fd, n_delete=1 )
