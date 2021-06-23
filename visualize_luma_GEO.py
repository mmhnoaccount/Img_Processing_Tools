import numpy as np
import cv2
import os
import re
import torch.nn as nn
import torch


height = 128
width = 128


A = np.zeros((128, 128), dtype=float)

f = open('A_162262661436_src1.txt')
lines = f.readlines()

count_line = 0
for line in lines:
    per_line = line.strip('\n').split(' ')
    A[count_line, 0:64] = per_line[0:64]
    count_line += 1
    
A = A / ((1 << 10) - 1)
A = A * 255
A = A.astype(np.uint8)
cv2.imshow('img', A)
