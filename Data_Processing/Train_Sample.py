import os
from tkinter import *
# import tkinter
# import tkinter.messagebox
import numpy as np
import cv2
from PIL import Image

def Train_Sample_Fun():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def getImagesAndLabels(path):
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        faceSamples=[]
        Ids=[]
        for imagePath in imagePaths:
            gray=Image.open(imagePath).convert('L')
            imageNp=np.array(gray,'uint8')
            Id=int(str(os.path.split(imagePath)).split("_")[0][-1])
            faces=detector.detectMultiScale(imageNp)
            for (x,y,w,h) in faces:
                faceSamples.append(imageNp[y:y+h,x:x+w])
                Ids.append(Id)
        # print(Ids)
        return faceSamples,Ids


    faces,Ids = getImagesAndLabels('Data')
    recognizer.train(faces, np.array(Ids))
    recognizer.save('trainer/trainer.yml')
    print("Data Trained")
    # dir=("Data")
    # path=[os.path.join(dir,file) for file in os.listdir(dir)]
    # faces=[]
    # ids=[]

    # for image in path:
    #     img=Image.open(image).convert('L')
    #     imagenp=np.array(img,'uint8')
    #     id=int(os.path.split(image)[1].split('_')[0])
    #     faces.append(imagenp)
    #     ids.append(id)
    #     cv2.imshow("training",imagenp)
    #     cv2.waitKey(1)==13
    # ids=np.array(ids) 
    # print(ids)   

    # clf=cv2.face.LBPHFaceRecognizer_create()
    # clf.train(faces,ids)
    # clf.write("classifier.yml")
    # cv2.destroyAllWindows()
    # tkinter.messagebox.showinfo("done","trained dataset")