import cv2
import numpy as np
import dlib
from imutils import face_utils
file_name="images/smile.jpeg"
gray=cv2.imread(file_name,0)
frame=cv2.imread(file_name)
face_detect = dlib.get_frontal_face_detector()
rects = face_detect(gray, 1)
for (i, rect) in enumerate(rects):
    (x, y, w, h) = face_utils.rect_to_bb(rect)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Video', frame)
cv2.waitKey(2000)