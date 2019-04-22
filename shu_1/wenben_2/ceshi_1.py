import csv,os

import os

file_path = "D:/test/test.py"
print(os.path.split(file_path)[0])
print(os.path.split(file_path)[1])

print(os.path.splitext(file_path)[0])
print(os.path.splitext(file_path)[1])

