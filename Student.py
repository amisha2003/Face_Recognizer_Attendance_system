from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("face Recognition System")

        #####variable########
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_class=StringVar()

        


        img1 = Image.open("E:\phtostemp\college_images\Stu.png")
        img1 = img1.resize((960,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label1 = Label(self.root,image=self.photoimg1)
        label1.place(x=0,y=0,width=960,height=200)

        img2 = Image.open("E:\phtostemp\college_images\Stu.png")
        img2 = img2.resize((960,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label2 = Label(self.root,image=self.photoimg2)
        label2.place(x=960,y=0,width=960,height=200)

#background image
        backimg = Image.open("E:\phtostemp\college_images\Th.jpg")
        backimg = backimg.resize((1920,880),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(backimg)

        label3 = Label(self.root,image=self.photoimg3)
        label3.place(x=0,y=200,width=1920,height=880)

#label
        title_lbl=Label(label3,text="Student Management System",font=("time new roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1920,height=50)
        

        main_frame=Frame(label3,bd=2)
        main_frame.place(x=10,y=55,width=1900,height=800)

#left label frame
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=900,height=700)

        img_left = Image.open("E:\phtostemp\college_images\Ab.jpeg")
        img_left = img_left.resize((900,200),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        labelimg_left = Label(left_frame,image=self.photoimg_left)
        labelimg_left.place(x=0,y=0,width=900,height=200)

#current cource
        left_frame2 = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("time new roman",12,"bold"))
        left_frame2.place(x=10,y=200,width=850,height=150)
    #Department   
        dep_label=Label(left_frame2,text='Department',font=("time new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(left_frame2,textvariable=self.var_dep,font=("time new roman",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("select Department","Computer Science","ECE","Civil","Mechanical","Architecture")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
    #Cource
        cource_label=Label(left_frame2,text='Department',font=("time new roman",12,"bold"),bg="white")
        cource_label.grid(row=0,column=2,padx=10)

        cource_combo=ttk.Combobox(left_frame2,textvariable=self.var_course,font=("time new roman",12,"bold"),width=17,state="read only")
        cource_combo["values"]=("select Cource","SE","FE","BE","TE","SE")
        cource_combo.current(0)
        cource_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
  #Year
        year_label=Label(left_frame2,text='Year',font=("time new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(left_frame2,textvariable=self.var_year,font=("time new roman",12,"bold"),width=17,state="read only")
        year_combo["values"]=("select Year","2020-21","2021-22","2022-23","2023-2024")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

  #Semester
        semester_label=Label(left_frame2,text='Semester',font=("time new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(left_frame2,textvariable=self.var_semester,font=("time new roman",12,"bold"),width=17,state="read only")
        semester_combo["values"]=("select Semester","Semester 1","Semester 2","Semester 3","Semester 4","Semester 5","Semester 6","Semester 7","Semester 8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        
#class student info
        class_student_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("time new roman",12,"bold"))
        class_student_frame.place(x=10,y=355,width=850,height=300)
#id
        studentid_label=Label(class_student_frame,text='StudentId:',font=("time new roman",12,"bold"),bg="white")
        studentid_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentid_entry=ttk.Entry(class_student_frame,textvariable=self.var_id,width=20,font=("times new roman",13,"bold"))
        studentid_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
#name
        studentname_label=Label(class_student_frame,text='Student Name:',font=("time new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
#class
        studentclass_label=Label(class_student_frame,text='Class Division:',font=("time new roman",12,"bold"),bg="white")
        studentclass_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("time new roman",12,"bold"),width=17,state="read only")
        class_combo["values"]=("select Division","a","b","c")
        class_combo.current(0)
        class_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
       
#roll
        studentroll_label=Label(class_student_frame,text='Roll No:',font=("time new roman",12,"bold"),bg="white")
        studentroll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentroll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        studentroll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
#gender
        studentgender_label=Label(class_student_frame,text='Gender:',font=("time new roman",12,"bold"),bg="white")
        studentgender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("time new roman",12,"bold"),width=17,state="read only")
        gender_combo["values"]=("select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

#dob
        studentdob_label=Label(class_student_frame,text='DOB:',font=("time new roman",12,"bold"),bg="white")
        studentdob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentdob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        studentdob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
#email
        studentemail_label=Label(class_student_frame,text='Email:',font=("time new roman",12,"bold"),bg="white")
        studentemail_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentemail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        studentemail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
#phone
        studentphone_label=Label(class_student_frame,text='Phone:',font=("time new roman",12,"bold"),bg="white")
        studentphone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentphone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        studentphone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
#address
        studentaddress_label=Label(class_student_frame,text='Address:',font=("time new roman",12,"bold"),bg="white")
        studentaddress_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        studentaddress_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        studentaddress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
#teacher
        studentteacher_label=Label(class_student_frame,text='Teacher Name:',font=("time new roman",12,"bold"),bg="white")
        studentteacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        studentteacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        studentteacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
#Radio Button
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take Photo Smple",value="Yes")
        radiobutton1.grid(row=5,column=0)

        radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Smple",value="NO")
        radiobutton2.grid(row=5,column=1)

#bbuttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=820,height=35)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=20,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        save_btn.grid(row=0,column=0)
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=20,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        update_btn.grid(row=0,column=1)
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=20,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        delete_btn.grid(row=0,column=2)
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=20,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,text="Take Photo",command=self.generate_dataset,width=20,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        take_photo_btn.grid(row=1,column=0)
        update_photo_btn=Button(btn_frame,text="Update Photo",width=20,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        update_photo_btn.grid(row=1,column=1)

        btn_frame2=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame2.place(x=0,y=240,width=820,height=35)
        take_photo_btn=Button(btn_frame2,text="Take Photo Sample",command=self.generate_dataset,width=40,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        take_photo_btn.grid(row=1,column=0)
        update_photo_btn=Button(btn_frame2,text="Reset Photo Sample",width=40,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        update_photo_btn.grid(row=1,column=1)

#right label frame
        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("time new roman",12,"bold"))
        right_frame.place(x=950,y=10,width=900,height=700)

        img_left1 = Image.open("E:\phtostemp\college_images\Ab.jpeg")
        img_left1 = img_left1.resize((900,200),Image.ANTIALIAS)
        self.photoimg_left1=ImageTk.PhotoImage(img_left1)

        labelimg_left1 = Label(right_frame,image=self.photoimg_left1)
        labelimg_left1.place(x=0,y=0,width=900,height=200)

#=======Search System==========#

        search_student_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,text="Search System",font=("time new roman",12,"bold"))
        search_student_frame.place(x=10,y=220,width=850,height=70)

        search_label=Label(search_student_frame,text='Search By:',font=("time new roman",15,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(search_student_frame,font=("time new roman",12,"bold"),width=17,state="read only")
        search_combo["values"]=("select","Roll No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_student_frame,width=20,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_student_frame,text="Search",width=12,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        search_btn.grid(row=0,column=3,padx=4)

        showall_btn=Button(search_student_frame,text="Show All",width=12,font=("time new roman",12,"bold"),bg="blue",fg="white",cursor="hand2")
        showall_btn.grid(row=0,column=4,padx=4)
#table frame
        table_frame = Frame(right_frame,bd=2,bg="white")
        table_frame.place(x=10,y=300,width=880,height=330)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")

        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    ############function declaration##################


    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="select Course" or self.var_year.get()=="select Year" or self.var_semester.get()=="select Semester" or self.var_id.get()=="" or self.var_dep.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_name.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Ami@1555",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),                                                                                                                
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{(str(es))}",parent=self.root)

############fetch data############
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="Ami@1555",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()
        
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#############get cursor##########
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

########update function##########

    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="select Course" or self.var_year.get()=="select Year" or self.var_semester.get()=="select Semester" or self.var_id.get()=="" or self.var_dep.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_name.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Ami@1555",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSampleStatus=%s where StudentId=%s",(
                                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                                    self.var_phone.get(),                                                                                                                
                                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                                    self.var_id.get(),
                                                                                                                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully update completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#########delete function#########
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Ami@1555",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where StudentId=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted Student",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


##########reset function#########
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_div.set("select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")



#################Generate data set or take a photo sample########################

    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get()=="select Course" or self.var_year.get()=="select Year" or self.var_semester.get()=="select Semester" or self.var_id.get()=="" or self.var_dep.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_gender.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_name.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Ami@1555",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSampleStatus=%s where StudentId=%s",(
                                                                                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                                                                                    self.var_semester.get(),
                                                                                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                                                                                    self.var_roll.get(),
                                                                                                                                                                                                                                                    self.var_gender.get(),
                                                                                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                                                                                    self.var_phone.get(),                                                                                                                
                                                                                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                                                                                    self.var_id.get()==id+1,
                                                                                                                                                                                                                                                ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()


                    ################Load Predefined data on face frontals from opencv################
                    face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_classifier.detectMultiScale(gray,1.3,5)
                        #Scaling factor=1.3
                        #minimum Neighbour=5


                        for (x,y,w,h) in faces:
                            face_cropped=img[y:y+h,x:x+w]
                            return face_cropped

                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                        ret,my_frame=cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id+=1
                            face=cv2.resize(face_cropped(my_frame),(450,450))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                            cv2.imwrite(file_name_path,face)
                            cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                            cv2.imshow("Cropped Face",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data sets completed!!!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
