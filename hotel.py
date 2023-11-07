from tkinter import *
from PIL import Image,ImageTk
from customer import cust_window
from room import room_book
from details import detailsroom



class HMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # -------------1st img---------------
        img1=Image.open(r"C:\Users\admin\Desktop\SE PRJ\photos\francesca-saraco-_dS27XGgRyQ-unsplash.jpg")
        img1=img1.resize((1550,140),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        # ----------------logo--------------
        img2=Image.open(r"C:\Users\admin\Desktop\SE PRJ\photos\vecteezy_vector-illustration-logo-grand-hotel-boutique-vintage-design_13087536.jpg")
        img2=img2.resize((230,140),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)

        # --------------title--------------
        lbl_title=Label(self.root,text="Hotel Management System",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)

        #-----------frame------------------
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        # --------------menu--------------
        lbl_menu=Label(main_frame,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        #-----------btn frame------------------
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_det,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        
        room_btn=Button(btn_frame,text="DETAILS",command=self.room_det,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        
        details_btn=Button(btn_frame,text="ROOM",command=self.details_room,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)
        
        # -------------right side image-------------
        img3=Image.open(r"C:\Users\admin\Desktop\SE PRJ\photos\louis-hansel-wVoP_Q2Bg_A-unsplash.jpg")
        img3=img3.resize((1310,590),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)

        #--------------down images-------------------
        img4=Image.open(r"C:\Users\admin\Desktop\SE PRJ\photos\qui-nguyen-giL2fHNr3Lc-unsplash.jpg")
        img4=img4.resize((230,210),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg2=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=225,width=230,height=210)

        img5=Image.open(r"C:\Users\admin\Desktop\SE PRJ\photos\rachel-park-hrlvr2ZlUNk-unsplash.jpg")
        img5=img5.resize((230,190),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg3=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg3.place(x=0,y=420,width=230,height=190)


    def cust_det(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_window(self.new_window)


    def room_det(self):
        self.new_window=Toplevel(self.root)
        self.app=room_book(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=detailsroom(self.new_window)


    def logout(self):
        self.root.destroy()



if __name__=="__main__":
    root=Tk()
    obj=HMS(root)
    root.mainloop()

