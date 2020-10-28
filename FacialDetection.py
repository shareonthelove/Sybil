import sys
import cv2

cam = cv2.CaptureVideo()
ifnot(cam.isOpened()): 
  print("No Camera Found!")
