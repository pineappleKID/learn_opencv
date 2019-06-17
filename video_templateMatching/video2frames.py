
import numpy as np
import cv2 as cv
fileName_in="Is China's Dominance in Table Tennis Real.avi"
cap=cv.VideoCapture(fileName_in)
frame_num=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    fileName_out='frames/'+str(frame_num).zfill(5)+'.png'
    cv.imwrite(fileName_out,frame)
    frame_num+=1
    if frame_num%200==0:
        print frame_num
cap.release()