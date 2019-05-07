# coding=utf-8
#把文件夹里面的文件的名字都改了
import os
dir = r'C:\Users\a7825\Desktop\工作空间\语音数据\CSJ\WAV\sp_fullcore_2\女\A01F0067分\8_A01F0067 - 副本'

name = os.listdir(dir)
na = 151#文件编号从几号开始
st = 'A01F0055'#文件名被改成了A01F0055_1,A01F0055_2...这种样子，按顺序这么排下去

dir_list = os.listdir(dir)
dir_list = sorted(dir_list,  key=lambda x: os.path.getmtime(os.path.join(dir, x)))#按照文件形成的时间顺序对文件名进行排序
for n in dir_list:
    newname = st + '_' + str(na) + '.wav'

    os.rename(os.path.join(dir, n), os.path.join(dir, newname))
    na += 1
    # os.system('pause')
    # os.rename(os.path.join(dir, n), os.path.join(dir, newname))
    # na += 1
