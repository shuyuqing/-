import os, os.path,shutil
import sys

path = r"C:\Users\a7825\Desktop\工作空间\语音数据\CSJ\WAV\sp_fullcore_2\女\A01F0067"
str_1 =r'A01F0055'#想要被改的部分
str_2 =r'A01F0067'#我想把str_1改成str_2

if __name__ == "__main__":

    for name in os.listdir(path):

        if str_1 in name:
            newname = name.replace(str_1,str_2)
            os.rename(os.path.join(path, name), os.path.join(path, newname))