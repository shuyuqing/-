#coding=utf-8
import os,shutil,os.path
import sys

str = ".wav"

newspeech_dir = "/home/shu/Desktop/data/RWCP-SP96/H_wav"

speech_dir = "/home/shu/Desktop/data/RWCP-SP96/H/"
#.ad文件所在的目录

if __name__ == "__main__":

     for ad_file in os.listdir(speech_dir):
        raw_file = speech_dir + ad_file.replace(".L16", ".raw")
        wav_file = speech_dir + ad_file.replace(".L16", ".wav")
        os.system("mv " + speech_dir + ad_file + " " + raw_file)
        os.system("sox -r 16000 -e s -b 16 -c 2 -x " + raw_file + " " + wav_file)#里面的2表示声道数

     for x in os.listdir(speech_dir):
        fp = os.path.join(speech_dir, x)

        if str in fp:
            #print(fp)

            newfp=os.path.join(newspeech_dir,os.path.basename(fp))
            shutil.move(fp,newfp)





