from cgitb import text
from email import message
from email.errors import MissingHeaderBodySeparatorDefect
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


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
        

        logintn=Button(main_frame,text="Login",font=("time new roman",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
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




        
 


if __name__ == "__main__":
    root=Tk()
    obj=register_window(root)
    root.mainloop()
