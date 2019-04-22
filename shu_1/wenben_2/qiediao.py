from pydub import AudioSegment
import os,csv

path_pici = r'C:\Users\a7825\Desktop\工作空间\语音数据\CSJ\WAV\第一批\新建文件夹'#批次

for filename in os.listdir(path_pici):

    path_wav = os.path.join(path_pici,filename,filename+'.wav')
    path_zhengjie = os.path.join(path_pici,filename,filename+'.txt')
    path_wav_2 = os.path.join(path_pici,filename,'wav')

    sound1 = AudioSegment.from_wav(path_wav)

    dakai = open(path_zhengjie, 'r', encoding='utf-8')
    txtwenjian = csv.reader(dakai)
    b = [i for i in txtwenjian]
    b_1 = []

    for y in b:
        u = y[0].split()
        xuhao=u[1].split('-')
        xuhao_1 = int(float(xuhao[0])*1000)
        xuhao_2 = int(float(xuhao[1])*1000)

        # print(xuhao_1)
        # print(xuhao_2)
        # os.system('pause')

        qiepian = sound1[xuhao_1:xuhao_2]
        path_wav_3 = os.path.join(path_wav_2, str(xuhao_1) + '_' + str(xuhao_2) + '_' + filename+'.wav')
        qiepian.export(path_wav_3, format='wav')

    dakai.close()

# with open(path_1, 'w',encoding='utf-8') as f:
#     for u in b_1:
#         f.writelines(u + '\n')  # 每写一句就空一行,把原来的文本都覆盖了
#
#
#
# duandian = [0,60094,120807,181332,246133,299441,360367,408006,485783,545951,613391,661682]
# jishuqi = 1
#
# for u in range(len(duandian)-1):
#     qiepian = sound1[duandian[u]+100:duandian[u+1]+100]
#     indir_2 = os.path.join(indir_1,str(duandian[u])+'_'+str(duandian[u+1])+ '_' + os.path.basename(indir))
#     jishuqi+=1
#     qiepian.export(indir_2, format='wav')





