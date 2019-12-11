#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import cv2
from time import sleep

# メイン関数
def main():
    image = cv2.imread('1dau.jpg') # ファイル読み込み

    # BGRでの色抽出
    bgrLower = np.array([17, 15, 150])    # 抽出する色の下限
    bgrUpper = np.array([128, 190, 255])    # 抽出する色の上限
    img_mask = cv2.inRange(image, bgrLower, bgrUpper)
    bgrResult = cv2.bitwise_and(image, image, mask=img_mask)
    cv2.imwrite('dautach.jpg', bgrResult)
    sleep(1)    

    while True:
        # キー入力を1ms待って、keyが「q」だったらbreak
        print ("ok");
        break


if __name__ == '__main__':
    main()
