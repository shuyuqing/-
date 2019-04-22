#coding=utf-8
import os,shutil,os.path
import sys

str = ".wav"


newspeech_dir = "/home/shu/Desktop/data/jnas/vol1/waves/m003/pb/wav/"

speech_dir = "/home/shu/Desktop/data/jnas/vol1/waves/m003/pb/raw/"
#.ad文件所在的目录

if __name__ == "__main__":

     for ad_file in os.listdir(speech_dir):
        raw_file = speech_dir + ad_file.replace(".ad", ".raw")
        wav_file = speech_dir + ad_file.replace(".ad", ".wav")
        os.system("mv " + speech_dir + ad_file + " " + raw_file)
        os.system("sox -r 16000 -e s -b 16 -c 1 -x " + raw_file + " " + wav_file)

     for x in os.listdir(speech_dir):
        fp = os.path.join(speech_dir, x)

        if str in fp:
            #print(fp)

            newfp=os.path.join(newspeech_dir,os.path.basename(fp))
            shutil.move(fp,newfp)





