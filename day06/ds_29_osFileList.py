# DATE : 20240219
# FILE : ds_29_osFileList.py
# DESC : 윈도우 파일 리스트

import os


fnameAry =[]
folderName = 'C:/Sources/ds-and-algorithm/day06'

for dirName, subDirList, fnames in os.walk(folderName):
    for fname in fnames:
        fnameAry.append(fname)

print(len(fnameAry))

print(fnameAry)
print(len(fnameAry))

fnameAry.sort(reverse=True)
print(fnameAry)