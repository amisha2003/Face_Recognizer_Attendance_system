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

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance System")
#variable
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_status=StringVar()

        img1 = Image.open("college_images\Ab.jpeg")
        img1 = img1.resize((960,300),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label1 = Label(self.root,image=self.photoimg1)
        label1.place(x=0,y=0,width=960,height=300)

        img2 = Image.open("college_images\Ab.jpeg")
        img2 = img2.resize((960,300),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label2 = Label(self.root,image=self.photoimg2)
        label2.place(x=960,y=0,width=960,height=300)

#label
        title_lbl=Label(self.root,text="Attendance",font=("time new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=300,width=1920,height=50)
        
        main_frame=Frame(self.root,bd=2)
        main_frame.place(x=10,y=350,width=1900,height=800)

#left label frame
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Attendance Details",font=("time new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=900,height=700)

        img_left = Image.open("E:\phtostemp\college_images\Ab.jpeg")
        img_left = img_left.resize((900,200),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        labelimg_left = Label(left_frame,image=self.photoimg_left)
        labelimg_left.place(x=0,y=0,width=900,height=200)
        

#class student info
        class_student_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("time new roman",12,"bold"))
        class_student_frame.place(x=10,y=200,width=850,height=400)

#Attendance_id
        Attendanceid_label=Label(class_student_frame,text='AttendanceId:',font=("time new roman",12,"bold"),bg="white")
        Attendanceid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        Attendanceid_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_id,font=("times new roman",13,"bold"))
        Attendanceid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
#roll
        studentroll_label=Label(class_student_frame,text='Roll No:',font=("time new roman",12,"bold"),bg="white")
        studentroll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentroll_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        studentroll_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
#name
        studentname_label=Label(class_student_frame,text='Student Name:',font=("time new roman",12,"bold"),bg="white")
        studentname_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_name,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

       
#department
        department_label=Label(class_student_frame,text='Department:',font=("time new roman",12,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        department_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_dep,font=("times new roman",13,"bold"))
        department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

#time
        Time_label=Label(class_student_frame,text='Time:',font=("time new roman",12,"bold"),bg="white")
        Time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Time_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_time,font=("times new roman",13,"bold"))
        Time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
#date
        Date_label=Label(class_student_frame,text='Date:',font=("time new roman",12,"bold"),bg="white")
        Date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Date_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_date,font=("times new roman",13,"bold"))
        Date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

#status
        Status_label=Label(class_student_frame,text='Attendance Status',font=("time new roman",12,"bold"),bg="white")
        Status_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        status_combo=ttk.Combobox(class_student_frame,textvariable=self.var_status,font=("Status",12,"bold"),width=17,state="read only")
        status_combo["values"]=("select Division","Present","Absent")
        status_combo.current(0)
        status_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
#bbuttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=820,height=35)

        import_btn=Button(btn_frame,text="Import.csv",command=self.importcsv,width=20,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        import_btn.grid(row=0,column=0)
        export_btn=Button(btn_frame,text="Export.csv",command=self.exportcsv,width=20,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        export_btn.grid(row=0,column=1)
        update_btn=Button(btn_frame,text="Update",width=20,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=2)
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        reset_btn.grid(row=0,column=3)

#right label frame
        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("time new roman",12,"bold"))
        right_frame.place(x=950,y=10,width=900,height=700)
        
        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=890,height=600)

        #######scroll bar table#######

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendance_table=ttk.Treeview(table_frame,column=("id","roll","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading("id",text="Attendance Id")
        self.attendance_table.heading("roll",text="Roll")
        self.attendance_table.heading("name",text="Name")
        self.attendance_table.heading("dep",text="Department")
        self.attendance_table.heading("time",text="Time")
        self.attendance_table.heading("date",text="Date")
        self.attendance_table.heading("attendance",text="Attendance Status")
        self.attendance_table["show"]="headings"

        self.attendance_table.column("id",width=100)
        self.attendance_table.column("roll",width=100)
        self.attendance_table.column("name",width=100)
        self.attendance_table.column("dep",width=100)
        self.attendance_table.column("time",width=100)
        self.attendance_table.column("date",width=100)
        self.attendance_table.column("attendance",width=100)

        self.attendance_table.pack(fill=BOTH,expand=1)
        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)
       


######fetch data###########

    def fetchdata(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)

    ####import csv####

    def importcsv(self):
        global mydata
        mydata.clear()
        fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fin) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)

    ####export#####

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fin,mode="w",newline="") as myFile:
                exp_write=csv.writer(myFile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fin)+" successfully",parent=self.root)
        
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{(str(es))}",parent=self.root)

        
    def get_cursor(self,event=""):
        cursor_focus=self.attendance_table.focus()
        content=self.attendance_table.item(cursor_focus)
        data=content["values"]

        self.var_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_dep.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_status.set(data[6]),

    def reset_data(self):
        self.var_id.set(""),
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_dep.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        self.var_status.set("Status")




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
