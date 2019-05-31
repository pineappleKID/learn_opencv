import cv2
import numpy as np
#import matplotlib.pyplot as plt
#import dlib
#from imutils import face_utils
font=cv2.FONT_HERSHEY_SIMPLEX
cascPath="/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
eyePath="/usr/local/share/OpenCV/haarcascades/haarcascade_eye.xml"
smilePath="/usr/local/share/OpenCV/haarcascades/haarcascade_smile.xml"
faceCascade=cv2.CascadeClassifier(cascPath)
eyeCascade=cv2.CascadeClassifier(eyePath)
smileCascade=cv2.CascadeClassifier(smilePath)

file_name="images/smile.jpeg"
frame = cv2.imread(file_name)
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray=cv2.imread(file_name,0)
faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,flags=cv2.CASCADE_SCALE_IMAGE)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]
    cv2.putText(frame,'Face',(x, y), font, 2,(255,0,0),5)

smile = smileCascade.detectMultiScale(roi_gray,scaleFactor= 1.16,minNeighbors=35,minSize=(25, 25),flags=cv2.CASCADE_SCALE_IMAGE)
for (sx, sy, sw, sh) in smile:
    cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (255, 0, 0), 2)#原文是cv2.rectangle(roi_color, (sh, sy), (sx+sw, sy+sh), (255, 0, 0), 2)
    cv2.putText(frame,'Smile',(x + sx,y + sy), 1, 1, (0, 255, 0), 1)
    print(smile)

eyes = eyeCascade.detectMultiScale(roi_gray)
for (ex,ey,ew,eh) in eyes:
    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.putText(frame,'Eye',(x + ex,y + ey), 1, 1, (0, 255, 0), 1)
cv2.putText(frame,'Number of Faces : ' + str(len(faces)),(40, 40), font, 1,(255,0,0),2)      
# Display the resulting frame
cv2.imshow('Video', frame)
cv2.waitKey(2000)