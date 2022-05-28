from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Developer System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("time new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1920,height=40)

        img_top = Image.open("college_images\Dev.jpg")
        img_top = img_top.resize((1920,1040),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        label1 = Label(self.root,image=self.photoimg_top)
        label1.place(x=0,y=40,width=1920,height=1040)
#frame
        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=1200,y=50,width=600,height=700)

        # img_my = Image.open("college_images\Amisha.jpg")
        # img_my = img_my.resize((200,200),Image.ANTIALIAS)
        # self.photoimg_my=ImageTk.PhotoImage(img_my)

        # label1 = Label(main_frame,image=self.photoimg_my)
        # label1.place(x=400,y=0,width=200,height=200)

        dev_lbl=Label(main_frame,text="Hello my name is Amisha Bharti",font=("time new roman",13,"bold"),bg="white",fg="blue")
        dev_lbl.place(x=0,y=5)
        dev_lbl=Label(main_frame,text="Hello my name is Amisha Bharti",font=("time new roman",13,"bold"),bg="white",fg="blue")
        dev_lbl.place(x=0,y=40)

        img2 = Image.open("college_images\KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img2 = img2.resize((600,500),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label2 = Label(main_frame,image=self.photoimg2)
        label2.place(x=0,y=210,width=600,height=500)

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()