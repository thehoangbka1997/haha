#encoding: utf8
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([0,100,0])
    upper_blue = np.array([5,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    red = cv2.bitwise_and(frame,frame, mask= mask)

    # グレースケール変換
    gray = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)

    # 2値化
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # ラベリング処理
    label = cv2.connectedComponentsWithStats(gray)

    # ブロブ情報を項目別に抽出
    n = label[0] - 1   #　ブロブの数
    data = np.delete(label[2], 0, 0)
    center = np.delete(label[3], 0, 0)  

    # ブロブ面積最大のインデックス
    try:
        max_index = np.argmax(data[:,4])
    # 面積最大ブロブの各種情報を表示
        center_max = center[max_index]
        x1 = data[:,0][max_index]
        y1 = data[:,1][max_index]
        x2 = x1 + data[:,2][max_index]  # x1 + 幅
        y2 = y1 + data[:,3][max_index]  # y2 + 高さ
        a = data[:,4][max_index]        # 面積
        result = cv2.rectangle(red, (x1, y1), (x2, y2), (0, 0, 255))
        cv2.imshow('frame',frame)
        cv2.imshow('red',result)
        if cv2.waitKey(1) & 0xFF == ord("q"):

            break
