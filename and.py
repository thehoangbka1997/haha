#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
src1 = cv2.imread('lena.jpg')
src2 = cv2.imread('ngua.jpg')

src2 = cv2.resize(src2, src1.shape[1::-1])

print(src2.shape)
# (225, 400, 3)

print(src2.dtype)
# uint8

dst = cv2.bitwise_and(src1, src2)

cv2.imwrite('and.jpg', dst)
