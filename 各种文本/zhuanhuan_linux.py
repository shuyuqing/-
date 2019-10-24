#coding=utf-8
import os,shutil,os.path
import sys

dir = r"/home/chen/dict/yuanwenjian"
#.ad文件所在的目录

if __name__ == "__main__":

     for ad_file in os.listdir(dir):
        os.system('iconv -f utf8 -t eucjp ~/dict/yuanwenjian/'+ad_file+' | yomi2voca.pl | iconv -f eucjp -t utf8 > ~/dict/zhuanhuawenjian/'+'zhuan_'+ad_file)#里面的2表示声道数





