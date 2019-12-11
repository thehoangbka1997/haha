#!/usr/bin/python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

im = cv2.imread("dautach.jpg")
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imwrite("xam.jpg", gray)

