import cv2
import os
import shutil
import numpy as np
'''
srcPackage = './all'
dstPackage1 = './321_481'
dstPackage2 = './481_321'

srcPackage = './sooor'
dstPackage1 = './other'
dstPackage2 = './648_648'

image_paths = os.listdir(srcPackage)
'''

def SizeClassification():
    for item in image_paths:
        img = cv2.imread(srcPackage + '/' + item)
        if img.shape[0] == 321 and img.shape[1] == 481:
            src = srcPackage + '/' + item
            dst = dstPackage1 + '/' + item
            shutil.copy(src, dst)
        elif img.shape[1] == 321 and img.shape[0] == 481:
            src = srcPackage + '/' + item
            dst = dstPackage2 + '/' + item
            shutil.copy(src, dst)


def crop():
    for item in image_paths:
        img = cv2.imread(srcPackage + '/' + item)
        if img.shape[0] < 648 or img.shape[1] < 648:
            src = srcPackage + '/' + item
            dst = dstPackage1 + '/' + item
            shutil.move(src, dst)
        else:
            src = srcPackage + '/' + item
            dst = dstPackage2 + '/' + item
            img = img[:648, :648, :]
            cv2.imwrite(dst, img)
            #shutil.copy(src, dst)


def cvtYUV420_and_Seq(package, seqFile):
    image_paths = os.listdir(package)
    fp = open(seqFile, "wb")
    for img_path in image_paths:
        img = cv2.imread(package + '/' + img_path)
        #print(img.shape)
        if img.shape[0] & 1:
            img = img[:-1, :, :]
        if img.shape[1] & 1:
            img = img[:, :-1, :]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV_I420)    ##图片尺寸不能为奇数
        img.tofile(fp)
    fp.close()


if __name__ =='__main__':
    
    package = './1352_1352'
    #package = './481_321'
    seqFile = '1352_1352.YUV'
    cvtYUV420_and_Seq(package, seqFile)
    
    #crop()
