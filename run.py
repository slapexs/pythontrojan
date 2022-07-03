import os
import random
import time
import shutil

# path  = r'd:\python trojan\test'
cwd = os.getcwd()
path = os.path.join(cwd, 'test')

folderList = os.listdir(path)

resultFolders = []
resultFiles = []



for fd in folderList:
    check = fd.split('.')
    if len(check) > 1:
        resultFiles.append(fd)
    else:
        resultFolders.append(fd)

fileDict = {}
for fi in resultFiles:
    select = random.choice(resultFolders)
    folderPath = os.path.join(path, select)
    filePath = os.path.join(folderPath, fi) # Path target
    currentPath = os.path.join(path, fi) # Current path

    fileDict[fi] = {'current': currentPath, 'next':filePath}
    # print(currentPath, '--->', filePath)


# Move file into folder
while True:
    for fk, fv in fileDict.items():
        currentPath = fv['current']
        nextPath = fv['next']
        shutil.move(currentPath, nextPath)

        select = random.choice(resultFolders)
        folderPath = os.path.join(path, select)
        fileNext = os.path.join(folderPath, fk)
        fileDict[fk]['current'] = nextPath
        fileDict[fk]['next'] = fileNext

    time.sleep(2)

print("Next:", fileDict)


