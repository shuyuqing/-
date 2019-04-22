import os

path = r"C:\Users\a7825\Desktop\工作空间\语音数据\ogvc_16\F1\B\wav_16"

newpath = r"C:\Users\a7825\Desktop\工作空间\语音数据\ogvc_16\F1\B"

str1 = r".wav"

if __name__ == "__main__":

    for name in os.listdir(path):
        print(name)
        newname = name.replace(str1, '')
        print(newname)
        with open(newpath+'\A.csv', 'a') as f:  # 将结果保存为result.csv
            f.write(newname + '\n')