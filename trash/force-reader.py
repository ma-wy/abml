#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import sys 
import time
import serial.tools.list_ports
from codecs import getincrementaldecoder
import numpy as np
import cv2

max_value = 45000

portx = "/dev/ttyUSB0"#in windows "COM4"
bps = 115200
timex = 5
ser = serial.Serial(portx, bps, timeout = timex)

while True:
  row = []
  col = []
  i = 0
  j = 0
  print(ser.read(19))
  '''
  for i in range(8):
    row = []
    j = 0
    for j in range(19):
      data = ser.read(1)
      if not data == b'\xff':
        row.append( int(data.hex(),16) )
      else:
        col.append(row[-16:])
  i = 0
  j = 0
  img = np.zeros((8,8))
  for i in range(8):
    j = 0
    for j in range(16):
      if j%2 == 1:
        img[i,int(j/2)] = col[i][j-1] *16*16 + col[i][j]
        #IndexError: list index out of range
  print(img[:,4:8])
  '''
  
#  image_arr = np.array(listdata)
#  cv2.imwrite("filename.png", image_arr)
#  i = 0
#  for i in range(8):
#    print(ser.read(19))
 
#  time.sleep(0.2)
