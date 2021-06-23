
import cv2
import numpy as np

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
            
    
if __name__ == '__name__':
    
