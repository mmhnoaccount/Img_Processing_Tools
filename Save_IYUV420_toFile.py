
import numpy as np
import cv2
import os
import re
import torch.nn as nn
import torch


def tryint(s):                       #将元素中的数字转换为int后再排序
    try:
        return int(s)
    except ValueError:
        return s

def str2int(v_str):                #将元素中的字符串和数字分割开
    return [tryint(sub_str) for sub_str in re.split('([0-9]+)', v_str)]

def sort_humanly(v_list):    #以分割后的list为单位进行排序
    return sorted(v_list, key=str2int)

def build_fullSize_Pic_luma(PicPackage):
    #height = 1352 // 2
    #width = 1352 // 2
    #height = 480 // 2
    #width = 832 // 2
    height = 1080 // 2
    width = 1920 // 2
    #height = 648 // 2
    #width = 648 // 2

    #A = np.zeros((height, width), dtype=float)
    A = np.zeros((1080, 1920), dtype=float)

    image_paths = os.listdir(PicPackage)
    image_paths = sort_humanly(image_paths)
    # print(image_paths)
    for j in range(width // 32):
        for i in range(height // 32):
            f = open(PicPackage + '/' + image_paths[j * (height // 32) + i])
            lines = f.readlines()
            '''
            block_row = i * 32
            for line in lines:
                per_line = line.strip('\n').split(' ')
                A[block_row, j * 32: j * 32 + 32] = per_line[:-1]
                block_row += 1
            '''
            block_row = i * 64
            count_line = 0
            for line in lines:
                count_line += 1
                
                # 当前块、左
                if count_line < 65:
                    continue
                
                '''
                # 上、左上
                if count_line > 64:
                    break
                '''
                
                per_line = line.strip('\n').split(' ')
                A[block_row, j * 64: j * 64 + 64] = per_line[64:-1]   #当前块、上
                # A[block_row, j * 64: j * 64 + 64] = per_line[0:64]  #左、左上
                block_row += 1
                
                

    A = A / ((1 << 10) - 1)
    A = A * 255
    A = A.astype(np.uint8)
    return A


def visualize_results_luma(path, fix=True):
    Luma = build_fullSize_Pic_luma(path)
    return Luma


def build_fullSize_Pic_chroma(PicPackage):
    #height = 1352 // 2
    #width = 1352 // 2
    #height = 480 // 2
    #width = 832 // 2
    height = 1080 // 2
    width = 1920 // 2
    #height = 648 // 2
    #width = 648 // 2

    A = np.zeros((height, width), dtype=float)

    image_paths = os.listdir(PicPackage)
    image_paths = sort_humanly(image_paths)
    # print(image_paths)
    for j in range(width // 32):
        for i in range(height // 32):
            f = open(PicPackage + '/' + image_paths[j * (height // 32) + i])
            lines = f.readlines()
            block_row = i * 32
            for line in lines:
                per_line = line.strip('\n').split(' ')
                A[block_row, j * 32: j * 32 + 32] = per_line[:-1]
                block_row += 1

    A = A / ((1 << 10) - 1)
    A = A * 255
    A = A.astype(np.uint8)
    return A


def visualize_results_chroma(path, fix=True):
    Cb = build_fullSize_Pic_chroma(path)
    return Cb


def build_fullSize_Pic_LM(PicPackage):
    #height = 1352 // 2
    #width = 1352 // 2
    #height = 480 // 2
    #width = 832 // 2
    height = 1080 // 2
    width = 1920 // 2
    #height = 648 // 2
    #width = 648 // 2

    A = np.zeros((height, width), dtype=float)

    image_paths = os.listdir(PicPackage)
    image_paths = sort_humanly(image_paths)
    # print(image_paths)
    for j in range(width // 32):
        for i in range(height // 32):
            f = open(PicPackage + '/' + image_paths[j * (height // 32) + i])
            lines = f.readlines()
            '''
            block_row = i * 32
            for line in lines:
                per_line = line.strip('\n').split(' ')
                A[block_row, j * 32: j * 32 + 32] = per_line[:-1]
                block_row += 1
            '''
            block_row = i * 32
            count_line = 0
            for line in lines:
                count_line += 1
                
                # 当前块、左
                if count_line < 33:
                    continue
                
                '''
                # 上、左上
                if count_line > 32:
                    break
                '''
                
                per_line = line.strip('\n').split(' ')
                A[block_row, j * 32: j * 32 + 32] = per_line[32:-1]   #当前块、上
                # A[block_row, j * 32: j * 32 + 32] = per_line[0:32]  #左、左上
                block_row += 1
                
                

    A = A / ((1 << 10) - 1)
    A = A * 255
    A = A.astype(np.uint8)
    return A


def visualize_results_LM(path, fix=True):
    Cr = build_fullSize_Pic_LM(path)
    return Cr



'''
输入Y，U，V三张图
保存为IYUV420格式的图片
'''
def Save_IYUV420(Y, U, V):
    height, width = Y.shape
    # print(Y.shape)
    # ret_img = np.zeros((height * 3 // 2, width), dtype=np.uint8)
    # print(ret_img.shape)
    
    # ret_img[0:height, 0:width] = Y
    
    U = U.reshape(-1, width)
    V = V.reshape(-1, width)
    ret_img = np.concatenate((Y, U, V), axis=0)
    # cv2.imshow("image", ret_img)
    # cv2.waitKey(0)
    # print(ret_img.shape)
    return ret_img


if __name__ == '__main__' :

    Y = visualize_results_luma(r'E:\YUV_Seqs\visualize_valid\Luma')
    U_org = visualize_results_chroma(r'E:\YUV_Seqs\visualize_valid\origCb')
    V_org = visualize_results_chroma(r'E:\YUV_Seqs\visualize_valid\origCr')

    YUV_org = Save_IYUV420(Y, U_org, V_org)

    path = './orig.yuv'
    f = open(path, "wb")
    YUV_org.tofile(f)
    f.close()


    U_LM = visualize_results_LM(r'E:\YUV_Seqs\visualize_valid\RecCb')
    V_LM = visualize_results_LM(r'E:\YUV_Seqs\visualize_valid\RecCr')
    YUV_LM = Save_IYUV420(Y, U_LM, V_LM)
    path = './LM.yuv'
    f = open(path, "wb")
    YUV_LM.tofile(f)
    f.close()
