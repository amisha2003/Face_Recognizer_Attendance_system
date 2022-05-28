from tkinter import*
from tkinter import ttk
import tkinter
import tkinter
from PIL import Image,ImageTk
import os
from Student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")
        

        img1 = Image.open("college_images\Stanford.jpg")
        img1 = img1.resize((960,250),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label1 = Label(self.root,image=self.photoimg1)
        label1.place(x=0,y=0,width=960,height=250)

        img2 = Image.open("college_images\Stanford.jpg")
        img2 = img2.resize((960,250),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label2 = Label(self.root,image=self.photoimg2)
        label2.place(x=960,y=0,width=960,height=250)
#background image
        backimg = Image.open("college_images\Th.jpg")
        backimg = backimg.resize((1920,880),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(backimg)

        label3 = Label(self.root,image=self.photoimg3)
        label3.place(x=0,y=250,width=1920,height=880)
#label
        title_lbl=Label(label3,text="Face Recognition Attendance System",font=("time new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1920,height=50)
        

#student button
        img4 = Image.open("college_images\Student.jpg")
        img4 = img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(label3,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b2=Button(label3,text="Student Detail",command=self.student_details,cursor="hand2",font=("time new roman",15,"bold"),bg="black",fg="white")
        b2.place(x=200,y=300,width=220,height=40)


#Detect Face button
        img5 = Image.open("college_images\Detector.jpg")
        img5 = img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b3=Button(label3,image=self.photoimg5,cursor="hand2",command=self.face_recognition)
        b3.place(x=600,y=100,width=220,height=220)

        b4=Button(label3,text="Face Detector",command=self.face_recognition,cursor="hand2",font=("time new roman",15,"bold"),bg="black",fg="white")
        b4.place(x=600,y=300,width=220,height=40)

#Attendance button
        img6 = Image.open("college_images\Attendance.jpg")
        img6 = img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b5=Button(label3,image=self.photoimg6,cursor="hand2",command=self.attendance_system)
        b5.place(x=1000,y=100,width=220,height=220)

        b6=Button(label3,text="Attendance",command=self.attendance_system,cursor="hand2",font=("time new roman",15,"bold"),bg="black",fg="white")
        b6.place(x=1000,y=300,width=220,height=40)

#Help button
        img7 = Image.open("college_images\Help.jpg")
        img7 = img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b7=Button(label3,image=self.photoimg7,cursor="hand2",command=self.help_system)
        b7.place(x=1400,y=100,width=220,height=220)

        b8=Button(label3,text="Help",command=self.help_system,cursor="hand2",font=("time new roman",15,"bold"),bg="black",fg="white")
        b8.place(x=1400,y=300,width=220,height=40)

#Train button
        img8 = Image.open("college_images\Train.jpg")
        img8 = img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b9=Button(label3,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b9.place(x=200,y=400,width=220,height=220)

        b10=Button(label3,text="Train Data",cursor="hand2",command=self.train_data,font=("time new roman",15,"bold"),bg="black",fg="white")
        b10.place(x=200,y=600,width=220,height=40)

#Photos button
        img9 = Image.open("college_images\Photo.png")
        img9 = img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b11=Button(label3,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b11.place(x=600,y=400,width=220,height=220)

        b12=Button(label3,text="Photos",command=self.open_img,cursor="hand2",font=("time new roman",15,"bold"),bg="black",fg="white")
        b12.place(x=600,y=600,width=220,height=40)

#Developer button
        img10 = Image.open("college_images\Developer.jpg")
        img10 = img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b13=Button(label3,image=self.photoimg10,cursor="hand2",command=self.developer_system)
        b13.place(x=1000,y=400,width=220,height=220)

        b14=Button(label3,text="Developer",command=self.developer_system,cursor="hand2",font=("time new roman",15,"bold"),bg="black",fg="white")
        b14.place(x=1000,y=600,width=220,height=40)

#Exit button
        img11 = Image.open("college_images\Exit.jpg")
        img11 = img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b15=Button(label3,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b15.place(x=1400,y=400,width=220,height=220)

        b16=Button(label3,text="Exit",cursor="hand2",command=self.iExit,font=("time new roman",15,"bold"),bg="black",fg="white")
        b16.place(x=1400,y=600,width=220,height=40)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
                self.root.destroy()
        else:
                return


#===============function buttons===============#

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def attendance_system(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer_system(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_system(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()