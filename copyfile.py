import os
import shutil
import time
cwd = os.getcwd()
path = os.path.join(cwd, 'test')

targetFile = os.path.join(path, 'dontopen.txt')

fileName = 'dontopen1.txt'
count = 1
while True:
    copyFile = os.path.join(path, fileName)
    shutil.copyfile(targetFile, copyFile)
    fileName = 'dontopen{}.txt'.format(count)
    count += 1
    time.sleep(2)
    