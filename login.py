from email import message
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import tkinter
import os
from Student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from developer import Developer
from help import Help


def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()


class login_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Login System")

        self.var_email=StringVar() 
        self.var_pass1=StringVar()

        img1 = Image.open("college_images\Stanford.jpg")
        img1 = img1.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label1 = Label(self.root,image=self.photoimg1)
        label1.place(x=0,y=0,width=1920,height=1080)

        main_frame=Frame(self.root,bd=2,bg="black")
        main_frame.place(x=600,y=200,width=600,height=600)

        login_lbl=Label(main_frame,text="LOGIN HERE",font=("time new roman",25,"bold"),bg="black",fg="red")
        login_lbl.place(x=200,y=30,width=200,height=50)

        main_frame1=Frame(main_frame,bd=2,bg="black")
        main_frame1.place(x=50,y=150,width=500,height=200)



#username
        username_label=Label(main_frame1,text='USERNAME:',font=("time new roman",20,"bold"),bg="black",fg="white")
        username_label.grid(row=1,column=0,padx=10,pady=20,sticky=W)

        self.username_entry=ttk.Entry(main_frame1,textvariable=self.var_email,width=40,font=("times new roman",20,"bold"))
        self.username_entry.grid(row=1,column=1,padx=10,pady=20,sticky=W)
#password
        password_label=Label(main_frame1,text='PASSWORD:',font=("time new roman",20,"bold"),bg="black",fg="white")
        password_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.password_entry=ttk.Entry(main_frame1,textvariable=self.var_pass1,width=40,font=("times new roman",20,"bold"))
        self.password_entry.grid(row=3,column=1,padx=10,pady=20,sticky=W)

##icon

        img2 = Image.open("college_images\LoginIconAppl.png")
        img2 = img2.resize((30,30),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label2 = Label(main_frame,image=self.photoimg2)
        label2.place(x=70,y=140,width=30,height=30)

        img3 = Image.open("college_images\Lock.png")
        img3 = img3.resize((30,30),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)                         

        label3 = Label(main_frame,image=self.photoimg3)
        label3.place(x=70,y=220,width=30,height=30)

        loginbtn=Button(main_frame,command=self.login1,text="Login",font=("time new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activebackground="red",activeforeground="white")
        loginbtn.place(x=200,y=370,width=200,height=55)

        registerbtn=Button(main_frame,text="New User Register",command=self.register_win,font=("time new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activebackground="red",activeforeground="white")
        registerbtn.place(x=50,y=460,width=200)
        
        passwordbtn=Button(main_frame,text="Forgot Password?",command=self.forgot_password_window,font=("time new roman",15,"bold"),borderwidth=0,fg="white",bg="black",activebackground="red",activeforeground="white")
        passwordbtn.place(x=50,y=490,width=200)
        


    def register_win(self):
        self.new_window=Toplevel(self.root)
        self.app=register_window(self.new_window)

    def login1(self):
        if self.username_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error","all field required")
        elif self.username_entry.get()=="kapu" and self.password_entry.get()=="123":
                messagebox.showinfo("Success","Welcome to Face Recognisation attendance system")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Ami@1555",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from register where email=%s and pass1=%s",(
                
                                                                                            self.var_email.get(),
                                                                                            self.var_pass1.get()
                                                                                        ))
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Username and Password")
                else:
                    open_main=messagebox.askyesno("YesNo","Access only Admin")
                    if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)
                    else:
                        if not open_main:
                            return
            


                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{(str(es))}",parent=self.root)

#####################reset password#####################################################################################

    def reset_pass(self):
        if self.security_combo.get()=="select":
            messagebox.showerror("Error","Select Security Question")
        elif self.security_entry.get()=="":
            messagebox.showerror("Error","Please Enter the Answer")
        elif self.newpass_entry.get()=="":
            messagebox.showerror("Error","Please Enter the new Password")

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Ami@1555",database="face_recognition")
            my_cursor=conn.cursor()
            query="selct * from register email=%s and securityQ=%s and securityA=%s"
            value=(self.username_entry.get(),self.security_combo.get(),self.security_entry)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the correct answer")
            else:
                qury=("update register set pass1=%s where email=%s")
                val=(self.password_entry.get(),self.username_entry.get())
                my_cursor.execute(qury,val)

                conn.commit()
                conn.close
                messagebox.showinfo("Info","Your Password has been reset , please login new password")





        
#####################forgot password window#############################################################################


    def forgot_password_window(self):
        if self.username_entry.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Ami@1555",database="face_recognition")
            my_cursor=conn.cursor()
            query="select * from register where email=%s"
            value=(self.username_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please enter the valid email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x600+610+170")

                l=Label(self.root2,text='Forget Password',font=("time new roman",20,"bold"),bg="black",fg="red")
                l.place(x=0,y=0,width=400,height=50)

                security_Q=Label(self.root2,text="Security Question:",font=("time new roman",20,"bold"),bg="white")
                security_Q.place(x=50,y=150)

                self.security_combo=ttk.Combobox(self.root2,font=("time new roman",12,"bold"),width=17,state="read only")
                self.security_combo["values"]=("select","Your Birth Place","Your Fathers name","Your Favourite food")
                self.security_combo.current(0)
                self.security_combo.place(x=50,y=200,width="300",height="40")
                        
                security_A=Label(self.root2,text="Security Answer:",font=("time new roman",20,"bold"),bg="white")
                security_A.place(x=50,y=250)

                self.security_entry=ttk.Entry(self.root2,font=("time new roman",20,"bold"))
                self.security_entry.place(x=50,y=300,width=300)
                

                newpass=Label(self.root2,text="New Password:",font=("time new roman",20,"bold"),bg="white")
                newpass.place(x=50,y=350)

                self.newpass_entry=ttk.Entry(self.root2,font=("time new roman",20,"bold"))
                self.newpass_entry.place(x=50,y=400,width=300)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("time new roman",20,"bold"),fg="white",bg="green")
                btn.place(x=100,y=500)








#######################################################Register##########################################

class register_window:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Login System")

         #####variable########
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass1=StringVar()
        self.var_pass2=StringVar()

        img1 = Image.open("college_images\Th.jpg")
        img1 = img1.resize((1920,1080),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        label1 = Label(self.root,image=self.photoimg1)
        label1.place(x=0,y=0,width=1920,height=1080)

        img2 = Image.open("college_images\Ph.jpg")
        img2 = img2.resize((500,850),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        label2 = Label(self.root,image=self.photoimg2)
        label2.place(x=100,y=100,width=500,height=850)

        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=600,y=100,width=1000,height=850)

        head_label=Label(main_frame,text='REGISTER HERE:',font=("time new roman",20,"bold"),bg="white",fg="green")
        head_label.place(x=0,y=20,w=350,h=50)

        ###############labels and entries############

        fname=Label(main_frame,text="First Name:",font=("time new roman",20,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(main_frame,textvariable=self.var_fname,font=("time new roman",20,"bold"))
        self.fname_entry.place(x=50,y=150,width=300)
        
        lname=Label(main_frame,text="Last Name:",font=("time new roman",20,"bold"),bg="white")
        lname.place(x=500,y=100)

        self.lname_entry=ttk.Entry(main_frame,textvariable=self.var_lname,font=("time new roman",20,"bold"))
        self.lname_entry.place(x=500,y=150,width=300)


        contact=Label(main_frame,text="Contact:",font=("time new roman",20,"bold"),bg="white")
        contact.place(x=50,y=250)

        self.contact_entry=ttk.Entry(main_frame,textvariable=self.var_contact,font=("time new roman",20,"bold"))
        self.contact_entry.place(x=50,y=300,width=300)

        
        email=Label(main_frame,text="Email:",font=("time new roman",20,"bold"),bg="white")
        email.place(x=500,y=250)

        self.email_entry=ttk.Entry(main_frame,textvariable=self.var_email,font=("time new roman",20,"bold"))
        self.email_entry.place(x=500,y=300,width=300)

        
        security_Q=Label(main_frame,text="Security Question:",font=("time new roman",20,"bold"),bg="white")
        security_Q.place(x=50,y=400)

        security_combo=ttk.Combobox(main_frame,textvariable=self.var_securityQ,font=("time new roman",12,"bold"),width=17,state="read only")
        security_combo["values"]=("select","Your Birth Place","Your Fathers name","Your Favourite food")
        security_combo.current(0)
        security_combo.place(x=50,y=450,width="300",height="40")
                
        security_A=Label(main_frame,text="Security Answer:",font=("time new roman",20,"bold"),bg="white")
        security_A.place(x=500,y=400)

        self.security_entry=ttk.Entry(main_frame,textvariable=self.var_securityA,font=("time new roman",20,"bold"))
        self.security_entry.place(x=500,y=450,width=300)

        password=Label(main_frame,text="Password:",font=("time new roman",20,"bold"),bg="white")
        password.place(x=50,y=550)

        self.password_entry=ttk.Entry(main_frame,textvariable=self.var_pass1,font=("time new roman",20,"bold"))
        self.password_entry.place(x=50,y=600,width=300)

        password2=Label(main_frame,text="Confirm Password:",font=("time new roman",20,"bold"),bg="white")
        password2.place(x=500,y=550)

        self.password2_entry=ttk.Entry(main_frame,textvariable=self.var_pass2,font=("time new roman",20,"bold"))
        self.password2_entry.place(x=500,y=600,width=300)

        #############check button###########
        
        self.var_check=IntVar()
        checkbtn=Checkbutton(main_frame,variable=self.var_check,text="I agree the Term and Condition",font=("time new roman",15,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=650)

        #########button#############

        registerbtn=Button(main_frame,text="Register",command=self.register_data,font=("time new roman",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
        registerbtn.place(x=50,y=740,width=200)
        

        logintn=Button(main_frame,text="Login",command=self.return_login,font=("time new roman",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
        logintn.place(x=500,y=740,width=200)


###########Function declaration############

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="select":
            messagebox.showerror("Error","All Fields are required")
        elif self.var_pass1.get()!=self.var_pass2.get():
            messagebox.showerror("Error","Password and confirm password muust be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree all Terms and Condition")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Ami@1555",database="face_recognition")
                my_cursor=conn.cursor()
                query="select * from register where email=%s"
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another mail")
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_fname.get(),
                                                                                                self.var_lname.get(),
                                                                                                self.var_contact.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_securityQ.get(),
                                                                                                self.var_securityA.get(),
                                                                                                self.var_pass1.get(),
                                                                                            ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Register details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{(str(es))}",parent=self.root)

    def return_login(self):
        self.root.destroy()

######################################################Face RECOGNITION#######################################################

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
    main()
