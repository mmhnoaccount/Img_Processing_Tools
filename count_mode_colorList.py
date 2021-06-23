
import os
import re
import matplotlib.pyplot as plt

file22 = 'Dec_record_22.txt'
file27 = 'Dec_record_27.txt'
file32 = 'Dec_record_32.txt'
file37 = 'Dec_record_37.txt'


useDPCM_List_count_22 = 0
useDPCM_List_count_27 = 0
useDPCM_List_count_32 = 0
useDPCM_List_count_37 = 0
useDPCM_List_count_all = 0

useOrig_count_22 = 0
useOrig_count_27 = 0
useOrig_count_32 = 0
useOrig_count_37 = 0
useOrig_count_all = 0

DPCM_PLTnum_22 = []
DPCM_PLTnum_27 = []
DPCM_PLTnum_32 = []
DPCM_PLTnum_37 = []
DPCM_PLTnum_all = []

Orig_PLTnum_22 = []
Orig_PLTnum_27 = []
Orig_PLTnum_32 = []
Orig_PLTnum_37 = []
Orig_PLTnum_all = []

DPCM_ResBitDepth_22 = []
DPCM_ResBitDepth_27 = []
DPCM_ResBitDepth_32 = []
DPCM_ResBitDepth_37 = []
DPCM_ResBitDepth_all = []

def Traverse_files(path, all_files=[]):
    global useDPCM_List_count_22 
    global useDPCM_List_count_27 
    global useDPCM_List_count_32 
    global useDPCM_List_count_37 
    global useDPCM_List_count_all 

    global useOrig_count_22 
    global useOrig_count_27 
    global useOrig_count_32 
    global useOrig_count_37
    global useOrig_count_all 

    global DPCM_PLTnum_22 
    global DPCM_PLTnum_27 
    global DPCM_PLTnum_32 
    global DPCM_PLTnum_37 
    global DPCM_PLTnum_all 

    global Orig_PLTnum_22 
    global Orig_PLTnum_27 
    global Orig_PLTnum_32 
    global Orig_PLTnum_37
    global Orig_PLTnum_all

    global DPCM_ResBitDepth_22 
    global DPCM_ResBitDepth_27 
    global DPCM_ResBitDepth_32 
    global DPCM_ResBitDepth_37 
    global DPCM_ResBitDepth_all 


    file_list = os.listdir(path)
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            # 递归
            Traverse_files(cur_path, all_files)
        else:
            if str(file) == file22:
                with open(cur_path) as f1:
                    lines = f1.readlines()

                for line in lines:
                    #print(line)
                    line = line.strip('\n').split(' ')
                    
                    if len(line) == 2:
                        if line[0] == 'useDPCM_List':
                            useDPCM_List_count_22 += 1
                            DPCM_PLTnum_22.append(int(line[1]))
                            useDPCM_List_count_all += 1
                            DPCM_PLTnum_all.append(int(line[1]))
                        elif line[0] == 'useOrig':
                            useOrig_count_22 += 1
                            Orig_PLTnum_22.append(int(line[1]))
                            useOrig_count_all += 1
                            Orig_PLTnum_all.append(int(line[1]))
                        elif line[0] == 'ResBitDepth':
                            DPCM_ResBitDepth_22.append(int(line[1]))
                            DPCM_ResBitDepth_all.append(int(line[1]))
            
            elif str(file) == file27:
                with open(cur_path) as f1:
                    lines = f1.readlines()

                for line in lines:
                    #print(line)
                    line = line.strip('\n').split(' ')
                    
                    if len(line) == 2:
                        if line[0] == 'useDPCM_List':
                            useDPCM_List_count_27 += 1
                            DPCM_PLTnum_27.append(int(line[1]))
                            useDPCM_List_count_all += 1
                            DPCM_PLTnum_all.append(int(line[1]))
                        elif line[0] == 'useOrig':
                            useOrig_count_27 += 1
                            Orig_PLTnum_27.append(int(line[1]))
                            useOrig_count_all += 1
                            Orig_PLTnum_all.append(int(line[1]))
                        elif line[0] == 'ResBitDepth':
                            DPCM_ResBitDepth_27.append(int(line[1]))
                            DPCM_ResBitDepth_all.append(int(line[1]))
                            
            elif str(file) == file32:
                with open(cur_path) as f1:
                    lines = f1.readlines()

                for line in lines:
                    #print(line)
                    line = line.strip('\n').split(' ')
                    
                    if len(line) == 2:
                        if line[0] == 'useDPCM_List':
                            useDPCM_List_count_32 += 1
                            DPCM_PLTnum_32.append(int(line[1]))
                            useDPCM_List_count_all += 1
                            DPCM_PLTnum_all.append(int(line[1]))
                        elif line[0] == 'useOrig':
                            useOrig_count_32 += 1
                            Orig_PLTnum_32.append(int(line[1]))
                            useOrig_count_all += 1
                            Orig_PLTnum_all.append(int(line[1]))
                        elif line[0] == 'ResBitDepth':
                            DPCM_ResBitDepth_32.append(int(line[1]))
                            DPCM_ResBitDepth_all.append(int(line[1]))
            
            elif str(file) == file37:
                with open(cur_path) as f1:
                    lines = f1.readlines()

                for line in lines:
                    #print(line)
                    line = line.strip('\n').split(' ')
                    
                    if len(line) == 2:
                        if line[0] == 'useDPCM_List':
                            useDPCM_List_count_37 += 1
                            DPCM_PLTnum_37.append(int(line[1]))
                            useDPCM_List_count_all += 1
                            DPCM_PLTnum_all.append(int(line[1]))
                        elif line[0] == 'useOrig':
                            useOrig_count_37 += 1
                            Orig_PLTnum_37.append(int(line[1]))
                            useOrig_count_all += 1
                            Orig_PLTnum_all.append(int(line[1]))
                        elif line[0] == 'ResBitDepth':
                            DPCM_ResBitDepth_37.append(int(line[1]))
                            DPCM_ResBitDepth_all.append(int(line[1]))
                


if __name__ == '__main__':
 
 
    Traverse_files('./')
    print('useDPCM_List : ', useDPCM_List_count_all)
    print('useOrig : ', useOrig_count_all)
    print()
    print('useDPCM_List_22 : ', useDPCM_List_count_22)
    print('useDPCM_List_27 : ', useDPCM_List_count_27)
    print('useDPCM_List_32 : ', useDPCM_List_count_32)
    print('useDPCM_List_37 : ', useDPCM_List_count_37)
    print()
    print('useOrig_22 : ', useOrig_count_22)
    print('useOrig_27 : ', useOrig_count_27)
    print('useOrig_32 : ', useOrig_count_32)
    print('useOrig_37 : ', useOrig_count_37)
    

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    fig, ax = plt.subplots()
    n, bins, patches = ax.hist(DPCM_PLTnum_37, x, density=True)
    n, bins, patches = ax.hist(Orig_PLTnum_37, x, density=True)
    n, bins, patches = ax.hist(DPCM_ResBitDepth_37, x, density=True)
    fig.tight_layout()
    plt.show()

    #print('DPCM_PLTnum : ', DPCM_PLTnum)
    #print('Orig_PLTnum : ', Orig_PLTnum)
    #print('DPCM_ResBitDepth : ', DPCM_ResBitDepth)
