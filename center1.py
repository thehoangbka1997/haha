#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

def main():
    # 入力画像の取得
    im = cv2.imread("dautach.jpg")
    
    # グレースケール変換
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # 2値化
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # ラベリング処理
    label = cv2.connectedComponentsWithStats(gray)

    # ブロブ情報を項目別に抽出
    n = label[0] - 1
    data = np.delete(label[2], 0, 0)
    center = np.delete(label[3], 0, 0)  

    # ブロブ面積最大のインデックス
    max_index = np.argmax(data[:,4])

    # 面積最大ブロブの各種情報を表示
    print("upper left x", data[:,0][max_index])
    print("upper left y", data[:,1][max_index])
    print("width", data[:,2][max_index])
    print("high", data[:,3][max_index])
    print("menA", data[:,4][max_index])
    print("center:",center[max_index])

if __name__ == '__main__':
    main()
