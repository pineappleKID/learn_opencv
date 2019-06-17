import numpy as np
import cv2 as cv
fileName_in="Is China's Dominance in Table Tennis Real.mp4"
fileName_out="Is China's Dominance in Table Tennis Real (filtered).avi"
fourcc = cv.VideoWriter_fourcc(*'XVID')
cap=cv.VideoCapture(fileName_in)
fps=cap.get( cv.CAP_PROP_FPS)
width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
out = cv.VideoWriter(fileName_out,fourcc, fps, (width,height))
frame_total=int(cap.get(cv.CAP_PROP_FRAME_COUNT))
for i in range(frame_total):
    imgName='frames/'+str(i).zfill(5)+'.png'
    img=cv.imread(imgName)
    out.write(img)
    if i%200==0:
        print i
cap.release()
out.release()