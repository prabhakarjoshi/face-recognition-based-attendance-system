import tkinter
import cv2


def Take_Sample_Fun(id):
    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    cap=cv2.VideoCapture(0)
    img_id=0
    while img_id<=100:
        ret,frame=cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces=face_classifier.detectMultiScale(gray,1.3,5)
        path="Data/"+str(id)+"_"+str(img_id)+".jpg"
        for(x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
            cv2.putText(frame," Image captured: "+str(img_id), (x-2,y+h-2),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),1)
            face=cv2.resize(frame[y:y+h,x:x+w],(450,450))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(path,face)

        if len(faces)>0:
            img_id+=1
        cv2.imshow("face",frame)
        if cv2.waitKey(1)==13:
            break
    tkinter.messagebox.showinfo("Success","Student added successfully")    

    cap.release()
    cv2.destroyAllWindows()
# Take_Sample_Fun()    
# 
