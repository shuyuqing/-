#wuyinqu:为了让julius更好地认识，在语音文件前后分别加上一段无音区间
from pydub import AudioSegment
import os,csv

path_2 = r'C:\Users\a7825\Desktop\无音区间/wuyin.wav'#无音区间的路径
indir = r'C:\Users\a7825\Desktop\工作空间\语音数据\CSJ\WAV\sp_fullcore_2\女\A01F0067'#存放语音数据的那个文件夹的位置
indir_1 = r'C:\Users\a7825\Desktop\工作空间\语音数据\CSJ\WAV\sp_fullcore_2\女\A01F0067无音'#拼接好的语音的位置

wuyin = AudioSegment.from_wav(path_2)

for file in os.listdir(indir):

    indir_2 = os.path.join(indir,file)
    sound1 = AudioSegment.from_wav(indir_2)
    sound2 = wuyin + sound1 + wuyin
    newfile = os.path.join(indir_1,file)
    sound2.export(newfile, format='wav')