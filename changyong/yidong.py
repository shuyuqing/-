import os, os.path,shutil
import sys

str = ".out"

path = r"C:\Users\a7825\Desktop\工作空间\语音数据\ogvc_16\M2\B\wav_16"

newpath = r"C:\Users\a7825\Desktop\工作空间\语音数据\ogvc_16\M2\B\keka"


if __name__ == "__main__":

    for x in os.listdir(path):
        fp = os.path.join(path, x)

        if str in fp:
            #print(fp)

            newfp=os.path.join(newpath,os.path.basename(fp))
            shutil.move(fp,newfp)
