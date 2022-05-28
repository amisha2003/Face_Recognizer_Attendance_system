from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import date, datetime
import cv2
import os
import numpy as np


class Face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="Face Recognition",font=("time new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1920,height=50)

        img_left = Image.open("college_images\Detector.jpg")
        img_left = img_left.resize((800,1030),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        label1 = Label(self.root,image=self.photoimg_left)
        label1.place(x=0,y=45,width=800,height=1030)

        img_right = Image.open("college_images\Facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_right = img_right.resize((1120,1000),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        label2 = Label(self.root,image=self.photoimg_right)
        label2.place(x=800,y=45,width=1120,height=1000)

        b2=Button(label2,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("time new roman",20,"bold"),bg="red",fg="white")
        b2.place(x=400,y=840,width=300,height=50)

###########Attendance###############

    def mark_attendance(self,i,r,n,d):
        with open("Amisha.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (n not in name_list) and (r not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")



###########face recognition#####

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            feature=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)
            coord=[]
            for (x,y,w,h) in feature:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                print(id)
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="Ami@1555",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where StudentId="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where StudentId="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Department from student where StudentId="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select StudentId from student where StudentId="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)

                


                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"StudentId:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videocap=cv2.VideoCapture(0)

        while True:
            ret,img=videocap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow('Welcome to Face Recognition',img)

            if cv2.waitKey(1)==13:
                break
        videocap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition(root)
    root.mainloop()
