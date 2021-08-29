import os
from tkinter import *
import tkinter
# import tkinter
# import tkinter.messagebox
import numpy as np
import cv2
from PIL import Image

def Train_Sample_Fun():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector= cv2.CascadeClassifier("Support/haarcascade_frontalface_default.xml")

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
    recognizer.save('Support/trainer.yml')
    # print("Data Trained")
    tkinter.messagebox.showinfo("done","trained dataset")
   
