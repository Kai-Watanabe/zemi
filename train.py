import chainer
import chainer.links as L
import chainer.functions as F
from chainer import training
from chainer.training import extensions
from chainer.datasets import TupleDataset
from sklearn.cross_validation import train_test_split
import numpy as np
import os
import model
import cv2

def getDate():

    #データを取り込み
    #取得先
    data_path1='./0_50x50/0'
    data_path2='./1_50x50/1'
    filelist1=os.listdir(data_path1)
    list1=len(filelist1)
    filelist2=os.listdir(data_path2)
    list2=len(filelist2)

    #読み
    for i j in filelist1, list1:
        X[j]=cv2.imread("%s/%s" % (data_path1, i), 0)
        #cv2.imshow('test', img_src1)
        #cv2.waitKey(100)
        y[j]=0
    for i j in filelist2, list2:
        X[j+list1]=cv2.imread("%s/%s" % (data_path2, i), 0)
        #cv2.imshow('test', img_src2)
        #cv2.waitKey(100)
        y[j+list1]=1

    X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.3, random_state=0)










def main():





    optimizer = optimizers.Adam()
    optimizer.setup(model)
