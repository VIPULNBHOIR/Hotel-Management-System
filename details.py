from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class detailsroom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        # --------------title--------------
        lbl_title=Label(self.root,text="room booking",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

         # ----------------logo--------------
        img2=Image.open(r"C:\Users\admin\Desktop\SE PRJ\photos\vecteezy_vector-illustration-logo-grand-hotel-boutique-vintage-design_13087536.jpg")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

           # -------------------label frame----------------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New room add",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)


         #floor
        lbl_floor=Label(labelframeleft,text="Floor : ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",13,"bold"))
        entry_floor.grid(row=0,column=1,sticky=W)

          #room no
        lbl_roomno=Label(labelframeleft,text="roomno : ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomno.grid(row=1,column=0,sticky=W)

        self.var_roomno=StringVar()
        entry_roomno=ttk.Entry(labelframeleft,textvariable=self.var_roomno,width=20,font=("arial",13,"bold"))
        entry_roomno.grid(row=1,column=1,sticky=W)

          #room type
        lbl_roomtype=Label(labelframeleft,text="roomtype : ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=2,column=0,sticky=W)

        self.var_roomtype=StringVar()
        entry_roomtype=ttk.Entry(labelframeleft,textvariable=self.var_roomtype,width=20,font=("arial",13,"bold"))
        entry_roomtype.grid(row=2,column=1,sticky=W)


        #--------------button--------------------
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndel=Button(btn_frame,text="delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndel.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)


          #--------------table frame search system---------------
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="show rooms",font=("times new roman",12,"bold"),padx=2)
        table_frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(table_frame,orient=VERTICAL)


        self.room_table=ttk.Treeview(table_frame,column=("floor","roomno",'roomtype'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_Y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Roomno")
        self.room_table.heading("roomtype",text="Roomtype")
      

        self.room_table["show"]='headings'
        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("error","all fields are required",parent=self.root)
        else:
            try:  
                conn=mysql.connector.connect(host="localhost",username="root",password="vipul",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values('%s','%s','%s')" %(
                                                                                    self.var_floor.get(),
                                                                                    self.var_roomno.get(),
                                                                                    self.var_roomtype.get()
      
                                                                                ))
                conn.commit()
                i=[self.var_floor.get(),self.var_roomno.get(),self.var_roomtype.get()]
                self.room_table.insert("",END,values=i)                                            
                conn.close()
                messagebox.showinfo("success","new room added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong : {str(es)}",parent=self.root)
        

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vipul",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
        
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0]),
        self.var_roomno.set(row[1]),
        self.var_roomtype.set(row[2])


    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("error","please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="vipul",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,roomno=%s,roomtype=% where roomno=%s",(
                                                                                    self.var_floor.get(),
                                                                                    self.var_roomno.get(),
                                                                                    self.var_roomtype.get(),
                                                                                  ))
            conn.commit()
            conn.close()
            messagebox.showinfo("update","New room details has been updated succesfully",parent=self.root)
            i=[self.var_floor.get(),self.var_roomno.get(),self.var_roomtype.get()]
            self.room_table.insert("",END,values=i)   
            selected_item = self.room_table.selection()[0]
            self.room_table.delete(selected_item)
    #delete
    def delete(self):
        delete=messagebox.askyesno("hotel management system","do you want delete this room details",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="vipul",database="management")
            my_cursor=conn.cursor()
            query="delete from details where roomno=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
            selected_item = self.room_table.selection()[0]
            self.room_table.delete(selected_item)
            messagebox.showinfo("update","customer details has been deleted succesfully",parent=self.root)
        else:
            if not delete:
                return
        conn.commit()
        conn.close()


    def reset(self):    #to fix the values of combobox we comment out them
        self.var_floor.set(""),
        self.var_roomno.set(""),
        self.var_roomtype.set("")


      










 













if __name__=="__main__":
    root=Tk()
    obj=detailsroom(root)
    root.mainloop()