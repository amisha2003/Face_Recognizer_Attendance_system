from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Train")

        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("time new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1920,height=40)

        img_top = Image.open("college_images\Facialrecognition.png")
        img_top = img_top.resize((1920,360),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        label1 = Label(self.root,image=self.photoimg_top)
        label1.place(x=0,y=40,width=1920,height=360)
        
        b2=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("time new roman",40,"bold"),bg="blue",fg="white")
        b2.place(x=0,y=400,width=1920,height=50)
        

        img_bottom = Image.open("college_images\Opencv.jpg")
        img_bottom = img_bottom.resize((1920,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        label2 = Label(self.root,image=self.photoimg_bottom)
        label2.place(x=0,y=450,width=1920,height=700)

    def train_classifier(self):
        data_dir=("data")        #folder name->data
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #Gray Scale Image
            imageNp=np.array(img,'uint8')   
            id1=int(os.path.split(image)[1].split('.')[1])
 
            faces.append(imageNp)
            ids.append(id1)
            cv2.imshow("Train",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)


        ###########train the classifier and save################

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")



if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()
