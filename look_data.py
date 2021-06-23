import numpy as np
import cv2
import os
import re

def tryint(s):                       #将元素中的数字转换为int后再排序
    try:
        return int(s)
    except ValueError:
        return s

def str2int(v_str):                #将元素中的字符串和数字分割开
    return [tryint(sub_str) for sub_str in re.split('([0-9]+)', v_str)]

def sort_humanly(v_list):    #以分割后的list为单位进行排序
    return sorted(v_list, key=str2int)



def look_a_block(width, height):
    A = np.zeros((height, width),dtype=float)    #先创建一个 3x3的全零方阵A，并且数据的类型设置为float浮点型
     
    f = open('32_32_32_32_1608641832_CCLM.txt')               #打开数据文件文件
    lines = f.readlines()           #把全部数据文件读到一个列表lines中
    A_row = 0                       #表示矩阵的行，从0行开始
    for line in lines:              #把lines中的数据逐行读取出来
        per_line = line.strip('\n').split(' ')      #处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
        #print(list)
        A[A_row, :] = per_line[:-1]                    #把处理后的数据放到方阵A中。list[0:3]表示列表的0,1,2列数据放到矩阵A中的A_row行
        A_row+=1                                #然后方阵A的下一行接着读
        #print(line)
     
    A = A / ((1 << 10) - 1)
    print(A)
    cv2.imshow('img', A)
    cv2.waitKey(0)

    
def look_a_Pic(width, height):
    A = np.zeros((height, width), dtype=float)
    
    PicPackage = r'E:\train_seq\Cb_32_32\MDLM_T'
    image_paths = os.listdir(PicPackage)
    image_paths = sort_humanly(image_paths)
    print(image_paths)
    for j in range(width//32):
        for i in range(height//32):           
            f = open(PicPackage + '/' + image_paths[j * (height//32) + i])               
            lines = f.readlines()           
            block_row = i * 32                       
            for line in lines:              
                per_line = line.strip('\n').split(' ')      
                A[block_row, j*32 : j*32+32] = per_line[:-1]                    
                block_row+=1                                
         
    A = A / ((1 << 10) - 1)
    print(A)
    cv2.imshow('img', A)
    cv2.waitKey(0)

if __name__ == '__main__':
    look_a_Pic(320 // 2, 480 // 2)
        
    
    
