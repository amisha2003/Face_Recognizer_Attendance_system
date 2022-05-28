import csv
from multiprocessing import parent_process
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog   

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Help System")

        img_top = Image.open("college_images\Help2.jpeg")
        img_top = img_top.resize((1920,1040),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        label1 = Label(self.root,image=self.photoimg_top)
        label1.place(x=0,y=0,width=1920,height=1040)

        dev_lbl=Label(label1,text="Email:bamisha814@gmail.com",font=("time new roman",30,"bold"),bg="white",fg="blue")
        dev_lbl.place(x=640,y=400,width=600,height=50)

if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()