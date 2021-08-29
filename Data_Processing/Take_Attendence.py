from DB.Mark_DB import Mark_DB_Fun
import cv2
from DB.Get_Name_DB import Get_Name_DB_Fun
def Take_Attendence_Fun():
    clf=cv2.face.LBPHFaceRecognizer_create()
    
    face_cascade=cv2.CascadeClassifier("Support/haarcascade_frontalface_default.xml")
    clf.read("Support/trainer.yml")
    a={}
    def draw_boundary(img,scalefactor,minneighbours):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=face_cascade.detectMultiScale(gray,scalefactor,minneighbours)

        for(x,y,w,h) in features:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
            id,predict=clf.predict(gray[y:y+h,x:x+w])
            confidence=int((100*(1-predict/300)))

            if confidence>70:
                a=Get_Name_DB_Fun(id)
                global myset
                myset=set()
                myset.add(id)
                cv2.putText(img,a, (x-2,y+h-2),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),1)

    def recog(img):
        draw_boundary(img,1.1,10)
        return img    

    
    video_cap=cv2.VideoCapture(0)
    while True:
        ret,img=video_cap.read()
        if img is not None:
            img=recog(img)
            cv2.imshow("welcome",img)
            if cv2.waitKey(1)==13:
                break
    # print(myset)  
    Mark_DB_Fun(myset)      
    video_cap.release()
    cv2.destroyAllWindows() 
