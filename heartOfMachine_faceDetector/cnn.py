import cv2
import numpy as np
import dlib
file_name="images/smile.jpeg"
gray=cv2.imread(file_name,0)
frame=cv2.imread(file_name)
dnnFaceDetector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
rects = dnnFaceDetector(gray, 1)
for (i, rect) in enumerate(rects):
    x1 = rect.rect.left()
    y1 = rect.rect.top()
    x2 = rect.rect.right()
    y2 = rect.rect.bottom()
    # Rectangle around the face
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the video output
cv2.imshow('Video', frame)
cv2.waitKey(2000)