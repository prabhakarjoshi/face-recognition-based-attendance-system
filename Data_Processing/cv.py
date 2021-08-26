import cv2
import os

face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cap=cv2.VideoCapture(0)
img_id=0
while img_id<=100:
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (127,0,255), 2)
        cv2.putText(frame,"Image captured: "+str(img_id), (x-2,y+h-2),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0),1)
    
    if len(faces)>0:
        img_id+=1
    cv2.imshow("face",frame)
    if cv2.waitKey(1)==13:
        break
    

cap.release()
cv2.destroyAllWindows()

