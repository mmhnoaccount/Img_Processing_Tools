import torch
import numpy as np

import tfrecord
from tfrecord.torch.dataset import TFRecordDataset


TrainSet_Pack = 'E:/File/package_by_mmh/train_set_128'
Train_Cb_org = TrainSet_Pack + '/origCb'
Train_Cr_org = TrainSet_Pack + '/origCr'
Train_Cb_rec = TrainSet_Pack + '/RecCb'
Train_Cr_rec = TrainSet_Pack + '/RecCr'
Train_Luma = TrainSet_Pack + '/Luma'
Train_QP = TrainSet_Pack + '/QPmask'

Train_Luma_list = os.listdir(Train_Luma)
Train_Cb_Rec_list = os.listdir(Train_Cb_rec)
Train_Cr_Rec_list = os.listdir(Train_Cr_rec)
Train_QP_list = os.listdir(Train_QP)

Train_Cb_org_list = os.listdir(Train_Cb_org)
Train_Cr_org_list = os.listdir(Train_Cr_org)

Train_len = len(Train_Luma_list)

Train_Luma_path = Train_Luma_list
Train_Chroma_path = (Train_Cb_Rec_list, Train_Cr_Rec_list)
Train_QP_path = Train_QP_list
Train_org_path = (Train_Cb_org_list, Train_Cr_org_list)


def Transform_Norm(features):
    features["image"] = cv2.imdecode(features["image"], -1)
    return features
    
    
def readMatrix(path, height, width, QP_mask=False):
    A = np.zeros((height, width), dtype=float)  # 先创建一个 3x3的全零方阵A，并且数据的类型设置为float浮点型

    f = open(path)  # 打开数据文件文件
    lines = f.readlines()  # 把全部数据文件读到一个列表lines中
    A_row = 0  # 表示矩阵的行，从0行开始
    for line in lines:  # 把lines中的数据逐行读取出来
        per_line = line.strip('\n').split(' ')  # 处理逐行数据：strip表示把头尾的'\n'去掉，split表示以空格来分割行数据，然后把处理后的行数据返回到list列表中
        # print(list)
        A[A_row, :] = per_line[:width]  # 把处理后的数据放到方阵A中。list[0:3]表示列表的0,1,2列数据放到矩阵A中的A_row行
        A_row += 1  # 然后方阵A的下一行接着读
        # print(line)
    # 等一下统一用transform来归一化
    if QP_mask:
        A = (A-(63.0/2.0)) / (63.0/2.0)
    else:
        A = (A-(1023.0/2.0)) / (1023.0/2.0)
    return A
    
    
  def catLuma(luma_path, index, Train, Visualize=False):
    if Visualize:
        Luma_Matrix = readMatrix(Visualize_Luma + '/' + luma_path[index], 128, 128)
    else:
        if Train:
            Luma_Matrix = readMatrix(Train_Luma + '/' + luma_path[index], 128, 128)
        else:
            Luma_Matrix = readMatrix(Test_Luma + '/' + luma_path[index], 128, 128)
    return np.expand_dims(Luma_Matrix, 0)

def catQP(qp_path, index, Train, Visualize=False):
    if Visualize:
        QP_Matrix = readMatrix(Visualize_QP + '/' + qp_path[index], 32, 32, QP_mask=True)
    else:
        if Train:
            QP_Matrix = readMatrix(Train_QP + '/' + qp_path[index], 32, 32, QP_mask=True)
        else:
            QP_Matrix = readMatrix(Test_QP + '/' + qp_path[index], 32, 32, QP_mask=True)
    return np.expand_dims(QP_Matrix, 0)

def catChroma(chroma_path, index, Train, Visualize=False):
    if Visualize:
        Cb_Matrix = readMatrix(Visualize_Cb_rec + '/' + chroma_path[0][index], 64, 64)
        Cr_Matrix = readMatrix(Visualize_Cr_rec + '/' + chroma_path[1][index], 64, 64)
        # QP_Matrix = readMatrix(Visualize_QP + '/' + chroma_path[2][index], QP_mask=True)
    else:
        if Train:
            Cb_Matrix = readMatrix(Train_Cb_rec + '/' + chroma_path[0][index], 64, 64)
            Cr_Matrix = readMatrix(Train_Cr_rec + '/' + chroma_path[1][index], 64, 64)
            # QP_Matrix = readMatrix(Visualize_QP + '/' + chroma_path[2][index], QP_mask=True)
        else:
            Cb_Matrix = readMatrix(Test_Cb_rec + '/' + chroma_path[0][index], 64, 64)
            Cr_Matrix = readMatrix(Test_Cr_rec + '/' + chroma_path[1][index], 64, 64)
            # QP_Matrix = readMatrix(Visualize_QP + '/' + chroma_path[2][index], QP_mask=True)
    return np.concatenate((np.expand_dims(Cb_Matrix, 0), np.expand_dims(Cr_Matrix, 0)), 0)


def catOrg(org_path, index, Train, Visualize=False):
    if Visualize:
        Cb_org_Matrix = readMatrix(Visualize_Cb_org + '/' + org_path[0][index], 32, 32)
        Cr_org_Matrix = readMatrix(Visualize_Cr_org + '/' + org_path[1][index], 32, 32)
    else:
        if Train:
            Cb_org_Matrix = readMatrix(Train_Cb_org + '/' + org_path[0][index], 32, 32)
            Cr_org_Matrix = readMatrix(Train_Cr_org + '/' + org_path[1][index], 32, 32)
        else:
            Cb_org_Matrix = readMatrix(Test_Cb_org + '/' + org_path[0][index], 32, 32)
            Cr_org_Matrix = readMatrix(Test_Cr_org + '/' + org_path[1][index], 32, 32)
    return np.concatenate((np.expand_dims(Cb_org_Matrix, 0), np.expand_dims(Cr_org_Matrix, 0)), 0)
  
    

def pics_to_TFRecord(luma_path, chroma_path, qp_path, org_path, size):    
    
    writer = tfrecord.TFRecordWriter("train.tfrecords")
    for i in range(1,size+1):
        print("----------processing the ",i,"\'th image----------")
        '''
        Luma_id = torch.FloatTensor(catLuma(self.luma_path, index, self.Train))
        Chorma_id = torch.FloatTensor(catChroma(self.chroma_path, index, self.Train))
        QP_id = torch.FloatTensor(catQP(self.qp_path, index, self.Train))
        org_id = torch.FloatTensor(catOrg(self.org_path, index, self.Train))
        '''
        Luma_id = catLuma(luma_path, i-1, self.Train)
        Chorma_id = catChroma(chroma_path, i-1, self.Train)
        QP_id = catQP(qp_path, i-1, self.Train)
        org_id = catOrg(org_path, i-1, self.Train)
        
        writer.write({'Luma': (Luma_id, 'float'), 
                    'Chorma': (Chorma_id, 'float'), 
                    'QP': (QP_id, 'float'), 
                    'org': (org_id, 'float')})
    writer.close()


if __name__ == '__main__':
    pics_to_TFRecord(Train_Luma_path, Train_Chroma_path, Train_QP_path, Train_org_path, Train_len)
