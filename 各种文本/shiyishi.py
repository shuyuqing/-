import os

RESULT_DIRS = 'C:/Users/a7825/Desktop/工作空间/语音数据/ASJ-JIPDEC/vol1/dat/can1001/h/keka'


if __name__ == '__main__':

 for file_name in os.listdir(RESULT_DIRS):
    # result_file_name 表示当前处理的识别结果文件 a01.out
     result_file_name = file_name.split('.')[0]
    #以“.”把文件名分开，[0]表示第一部分

     print(result_file_name)
     print(result_file_name[1])