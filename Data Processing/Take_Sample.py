import cv2
import os

face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def crop(img):
    # gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(img,1.3,5)

    for(x,y,w,h) in faces:
        crop=img[y:y+h,x:x+w]
        return crop        

cap=cv2.VideoCapture(0)
img_id=0
while True:

    ret,frame=cap.read()
    if crop(frame) is not None:
        img_id+=1
    face=crop(frame)    
    # face=cv2.resize(im,450,450)

    # face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
    file_name="data/user."+str(id)+"."+str(img_id)+".jpg"
    # cv2.imwrite(filename=file_name)
    # cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
    cv2.imshow("face",face)
    if cv2.waitKey(1)==13 or int(img_id)==100:
        break
cap.release()
cv2.destroyAllWindows()