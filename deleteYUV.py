
# 导入需要的库
import os
import re


# 子函数，显示所有文件的路径
def show_files(path, all_files):
    # 显示当前目录所有文件和子文件夹，放入file_list数组里
    file_list = os.listdir(path)
    # 循环判断每个file_list里的元素是文件夹还是文件，是文件的话，把名称传入list，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量
        cur_path = os.path.join(path, file)
        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            # 递归
            show_files(cur_path, all_files)
        else:
            # 将file添加进all_files里
            # all_files.append(file)
            #if str(file) == 'rec_' + r'/d/d' + '.yuv' or str(file) == 'dec_/d/d.yuv':
            ret1 = re.search('rec_\d*\.yuv', str(file))
            ret2 = re.search('dec_\d*\.yuv', str(file))
            if ret1 or ret2:
                os.remove(cur_path)
                # all_files.append(cur_path)
    return all_files
    
    
if __name__ == '__main__' :
    # 以下是主程序
    # 传入空的list接收文件名
    contents = show_files("./", [])
    
    '''
    # 循环打印show_files函数返回的文件名列表
    for content in contents:
        print(content)
    '''




    
