import numpy as np
import cv2

def two():
    
    faceCascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,     
            scaleFactor=1.2,
            minNeighbors=10,     
            minSize=(20, 20)
        )
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]  
        cv2.imshow('video',img)
        if  cv2.waitKey(1) & 0xff == ord('q'):
          break      
    cap.release()
    cv2.destroyAllWindows()
