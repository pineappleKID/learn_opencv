import numpy as np
import cv2 as cv
fileName_in="Is China's Dominance in Table Tennis Real.mp4"
fileName_out="Is China's Dominance in Table Tennis Real.avi"
fourcc = cv.VideoWriter_fourcc(*'XVID')
cap=cv.VideoCapture(fileName_in)
fps=cap.get( cv.CAP_PROP_FPS)
width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
out = cv.VideoWriter(fileName_out,fourcc, fps, (width,height))
template=cv.imread('flag1.bmp',0)
to_switch=cv.imread('flag2.bmp')
w, h = template.shape[::-1]

frame_num=0
frame_total=cap.get(cv.CAP_PROP_FRAME_COUNT)
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    frame_num+=1
    img_gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        frame[pt[1]:pt[1]+h,pt[0]:pt[0]+w]=to_switch
        #cv.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,0), 2)
    out.write(frame)
    if frame_num %200 == 0:
        print frame_num,'/',frame_total
cap.release()
out.release()

    
