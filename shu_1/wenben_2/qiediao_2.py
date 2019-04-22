from pydub import AudioSegment
import os,csv

path = r"C:\Users\a7825\Desktop\工作空间\语音数据\RWCP-SP96-要切\垃圾\新建文件夹"#批次

# indir_1 = os.path.join(indir,)
# indir_2 = os.path
# sound1_l = AudioSegment.from_wav(indir_l)
# sound2_r = AudioSegment.from_wav(indir_r)

for filename in os.listdir(path):

    path_2 = os.path.join(path,filename,'wav_all')
    wavleft = os.path.join(path_2,'left_'+filename+'.wav')
    wavright = os.path.join(path_2,'right_'+filename+'.wav')

    sound1_l = AudioSegment.from_wav(wavleft)
    sound1_r = AudioSegment.from_wav(wavright)

    path_zhengjie = os.path.join(path,filename,filename+'_1'+'.txt')
    dakai = open(path_zhengjie, 'r', encoding='utf-8')

    txtwenjian = csv.reader(dakai)
    b = [i for i in txtwenjian]

    for n in range(len(b)):

        print(filename)
        print(n)
        if b[n] != '':
            if b[n][0] == 'B':#记住B是left

                xuhao1_b = b[n+1][0]
                xuhao2_b = b[n+2][0]
                # print("现在输出b序号")
                # print(xuhao1_b)
                # print(xuhao2_b)
                # os.system("pause")
                qiepian_l = sound1_l[int(xuhao1_b):int(xuhao2_b)]
                path_wav = os.path.join(path,filename, 'wav','l_'+str(xuhao1_b) + '_' + str(xuhao2_b) + '_' + filename + '.wav')
                qiepian_l.export(path_wav, format='wav')

            elif b[n][0] == 'A':#A是right

                xuhao1_a = b[n+1][0]
                xuhao2_a = b[n+2][0]
                # print("现在输出a序号")
                # print(xuhao1_a)
                # print(xuhao2_a)
                # os.system("pause")
                qiepian_r = sound1_r[int(xuhao1_a):int(xuhao2_a)]
                path_wav = os.path.join(path,filename, 'wav','r_'+str(xuhao1_a) + '_' + str(xuhao2_a) + '_' + filename + '.wav')
                qiepian_r.export(path_wav, format='wav')

    dakai.close()







