#!/usr/bin/env python
#encoding: utf8
import numpy as np
import cv2
from time import sleep

# メイン関数
def main():
    image = cv2.imread('1dau.jpg') # ファイル読み込み

    # HSVでの色抽出
    hsvLower = np.array([0, 100, 0])    # 抽出する色の下限
    hsvUpper = np.array([5, 255, 255])    # 抽出する色の上限
    hsvResult = hsvExtraction(image, hsvLower, hsvUpper)
    cv2.imwrite('dautach1.jpg', hsvResult)
    sleep(1)

    while True:
        print ('ok')
        break   

def hsvExtraction(image, hsvLower, hsvUpper):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # 画像をHSVに変換
    hsv_mask = cv2.inRange(hsv, hsvLower, hsvUpper)    # HSVからマスクを作成
    result = cv2.bitwise_and(image, image, mask=hsv_mask) # 元画像とマスクを合成
    return result


if __name__ == '__main__':
    main()
