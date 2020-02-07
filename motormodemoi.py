#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import sleep
import RPi.GPIO as GPIO

DIR = 17       # Direction GPIO Pin
STEP = 27      # Step GPIO Pin
CW = 1         # Clockwise Rotation
CCW = 0        # Counterclockwise Rotation
SPR = 200       # Steps per Revolution (360 / 1.8)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

MODE = (14, 15, 18) # Microstep Resolution GPIO Pins
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full': (0, 0, 0),
              'Half': (1, 0, 0),
              '1/4': (0, 1, 0),
              '1/8': (1, 1, 0),
              '1/16': (0, 0, 1),
              '1/32': (1, 0, 1)}

GPIO.output(MODE, RESOLUTION['Full'])

step_count = SPR * 1
delay = .005 / 4

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR, CCW)

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)


GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)
GPIO.output(DIR2, CW)
DIR2 = 23       # Direction GPIO Pin
STEP2 = 24      # Step GPIO Pin
for x in range(step_count):
    GPIO.output(STEP2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR2, CCW)

for x in range(step_count):
    GPIO.output(STEP2, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP2, GPIO.LOW)
    sleep(delay)


GPIO.cleanup()
