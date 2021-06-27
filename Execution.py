import cv2
import numpy as np
import os
import sys
import webbrowser as wb
def six():
    user_id ={
    "N160082": 'sameer',
    "N160150": 'Surya',
    "N160235": 'Dhanu',
    }
    x=str(input('Enter your user_id: '))
    b=user_id[x]
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "cascades/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX#iniciate id counter
    id = 0# names related to ids: example ==> Marcelo: id=1,  etc
    names = ['None','sameer','Surya'] # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height# Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    while True:
        ret, img =cam.read()
        
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
           )
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                    # If confidence is less them 100 ==> "0" : perfect match 
            if (confidence >= 60):
                id = names[id]
                confidence = "  {0}%".format(round(100 - confidence))
                g=id
                print (g)
                if b==g:
                    print('Hii',b)
                    print('file opening')
                    wb.open_new(r'C:\Users\Raja\Desktop\sam video\sam.pdf')
                    cam.release()
                    cv2.destroyAllWindows()
                else :
                    print('Wrong person')
                    sys.exit()

            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))
                
six()
      


