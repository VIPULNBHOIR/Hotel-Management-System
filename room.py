from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class room_book:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #-------------------variables---------------------
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
      


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
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="room details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #------------------labels and entrys-----------------------------
        lbl_cust_contact=Label(labelframeleft,text="customer contact : ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)

        #fetch data button
        btnfetchdata=Button(labelframeleft,command=self.fetch_contactdata,text="fetch data",font=("arial",12,"bold"),bg="black",fg="gold",width=8)
        btnfetchdata.place(x=330,y=4)


        check_in_date=Label(labelframeleft,text="check in date : ",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txt_checkin_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        txt_checkin_date.grid(row=1,column=1)


        check_out_date=Label(labelframeleft,text="check out date : ",font=("arial",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2,column=0,sticky=W)
        txt_checkout_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
        txt_checkout_date.grid(row=2,column=1)


        lbl_roomtype=Label(labelframeleft,text="room type : ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomtype.grid(row=3,column=0,sticky=W)

        id=["luxury","single","double"]

        combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="read only")
        combo_roomtype["value"]=id
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1)

        lbl_roomavailable=Label(labelframeleft,text="available room : ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_roomavailable.grid(row=4,column=0,sticky=W)
        # txt_roomavailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
        # txt_roomavailable.grid(row=4,column=1)

        conn=mysql.connector.connect(host="localhost",username="root",password="vipul",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomno from details")
        rows=my_cursor.fetchall()
        combo_roomno=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=27,state="read only")
        combo_roomno["value"]=rows
        combo_roomno.current(0)
        combo_roomno.grid(row=4,column=1)


        lbl_meal=Label(labelframeleft,text="meal : ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_meal.grid(row=5,column=0,sticky=W)
        jd=["lunch","breakfast"]
        combo_meal=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",12,"bold"),width=27,state="read only")
        combo_meal["value"]=jd
        combo_meal.current(0)
        combo_meal.grid(row=5,column=1)

        lbl_noofdays=Label(labelframeleft,text="no of days : ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_noofdays.grid(row=6,column=0,sticky=W)
        txt_noofdays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
        txt_noofdays.grid(row=6,column=1)

        lbl_noofdays=Label(labelframeleft,text="paid tax : ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_noofdays.grid(row=7,column=0,sticky=W)
        txt_noofdays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"))
        txt_noofdays.grid(row=7,column=1)

        lbl_noofdays=Label(labelframeleft,text="sub total : ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_noofdays.grid(row=8,column=0,sticky=W)
        txt_noofdays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",13,"bold"))
        txt_noofdays.grid(row=8,column=1)

        lbl_idnumber=Label(labelframeleft,text="total cost : ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_idnumber.grid(row=9,column=0,sticky=W)
        txt_idnumber=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
        txt_idnumber.grid(row=9,column=1)

        #--------------bill button-------------------
        btnbill=Button(labelframeleft,text="bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnbill.grid(row=10,column=0,padx=1,sticky=W)


        #--------------button--------------------
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndel=Button(btn_frame,text="delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndel.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

        #rightside image

        img3=Image.open(r"C:\Users\admin\Desktop\SE PRJ\photos\qui-nguyen-giL2fHNr3Lc-unsplash.jpg")
        img3=img3.resize((520,200),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=200)







         #--------------table frame search system---------------
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="view details and searcch system",font=("times new roman",12,"bold"),padx=2)
        table_frame.place(x=435,y=280,width=860,height=260)

        lblsearchby=Label(table_frame,text="search by : ",font=("arial",12,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="read only")
        combo_search["value"]=("contact","roomavailable")
        combo_search.grid(row=0,column=1,padx=2)


        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtsearch.grid(row=0,column=2,padx=2)


        btnsearch=Button(table_frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall=Button(table_frame,text="Show all",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnshowall.grid(row=0,column=4,padx=1)



        #------------show DATA table--------------
        detail_table=LabelFrame(table_frame,bd=2,relief=RIDGE,text="view details and searcch system",font=("times new roman",12,"bold"),padx=2)
        detail_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(detail_table,orient=VERTICAL)


        self.room_table=ttk.Treeview(detail_table,column=("contact","checkin",'checkout','roomtype','roomavailable','meal','noofdays'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_Y.config(command=self.room_table.yview)




        self.room_table.heading("contact",text="contact")
        self.room_table.heading("checkin",text="check-in")
        self.room_table.heading("checkout",text="check-out")
        self.room_table.heading("roomtype",text="room-type")
        self.room_table.heading("roomavailable",text="room no")
        self.room_table.heading("meal",text="meal")
        self.room_table.heading("noofdays",text="noofdays")
    

        self.room_table["show"]='headings'
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("error","all fields are required",parent=self.root)
        else:
            try:  
                conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room1 values('%s','%s','%s','%s','%s','%s','%s')" %(
                                                                                    self.var_contact.get(),
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomavailable.get(),
                                                                                    self.var_meal.get(),
                                                                                    self.var_noofdays.get()
      
                                                                                ))
                conn.commit()
                i=[self.var_contact.get(),self.var_checkin.get(),self.var_checkout.get(), self.var_roomtype.get(),self.var_roomavailable.get(), self.var_meal.get(),self.var_noofdays.get()]
                self.room_table.insert("",END,values=i)                                            
                conn.close()
                messagebox.showinfo("success","room booked ",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong : {str(es)}",parent=self.root)
    
    #fetch data
    def fetch_data(self):
        try:
            for item in self.room_table.get_children():
                self.room_table.delete(item)
        except:
            pass
        conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room1")
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

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])

    #update function
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("error","please enter floor number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update room1 set chech_in='%s',check_out='%s',roomtype='%s',roomavailable='%s',meal='%s',noofdays='%s' where contact='%s'" %(
                                                                                                                                                            self.var_checkin.get(),
                                                                                                                                                            self.var_checkout.get(),
                                                                                                                                                            self.var_roomtype.get(),
                                                                                                                                                            self.var_roomavailable.get(),
                                                                                                                                                            self.var_meal.get(),
                                                                                                                                                            self.var_noofdays.get(),
                                                                                                                                                            self.var_contact.get()
                                                                                                                                                    
                                                                                                                                                                            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("update","room details has been added succesfully",parent=self.root)
            i=[self.var_contact.get(),self.var_checkin.get(),self.var_checkout.get(), self.var_roomtype.get(),self.var_roomavailable.get(), self.var_meal.get(),self.var_noofdays.get()]
            self.room_table.insert("",END,values=i)                                            
            selected_item = self.room_table.selection()[0]
            self.room_table.delete(selected_item)

    #delete
    def delete(self):
        delete=messagebox.askyesno("hotel management system","do you want delete this customer",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
            my_cursor=conn.cursor()
            query="delete from room1 where contact=%s"
            value=(self.var_contact.get(),)
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
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
    



    #==============fetch all data===============
    def fetch_contactdata(self):
        if self.var_contact.get()=="":
            messagebox.showerror("error","please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
            my_cursor=conn.cursor()
            query=("select custname from customer2 where mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("error","this number not found",parent=self.root)
            else:
                print(row)
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblname=Label(showDataframe,text="name : ",font=("arial",12,"bold"))
                lblname.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
                my_cursor=conn.cursor()
                query=("select gender from customer2 where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


                lblgender=Label(showDataframe,text="gender : ",font=("arial",12,"bold"))
                lblgender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)



                conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
                my_cursor=conn.cursor()
                query=("select email from customer2 where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


                lblemail=Label(showDataframe,text="email : ",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)


                conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
                my_cursor=conn.cursor()
                query=("select nationality from customer2 where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


                lblnatlty=Label(showDataframe,text="nationality : ",font=("arial",12,"bold"))
                lblnatlty.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)


                conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
                my_cursor=conn.cursor()
                query=("select address from customer2 where mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()


                lbladd=Label(showDataframe,text="address : ",font=("arial",12,"bold"))
                lbladd.place(x=0,y=120)

                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)

    #search system
    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room1 where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        print("select * from room1 where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        print(self.txt_search.get())
        rows=my_cursor.fetchall()
        print(rows)
        if len(rows)!=0:
            for item in self.room_table.get_children():
                self.room_table.delete(item)
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def total(self):
        #inDate=self.var_checkin.get()
        #outDate=self.var_checkout.get()
        #inDate=datetime.strptime(inDate,"%D/%M/%Y")
        #outDate=datetime.strptime(outDate,"%D/%M/%Y")
        #self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            St="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(St)
            self.var_total.set(total)



        
        elif(self.var_meal.get()=="lunch" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            St="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(St)
            self.var_total.set(total)


        
        elif(self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="double"):
            q1=float(500)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            St="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(St)
            self.var_total.set(total)

        elif(self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            St="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(St)
            self.var_total.set(total)



        
        elif(self.var_meal.get()=="lunch" and self.var_roomtype.get()=="double"):
            q1=float(400)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            St="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(St)
            self.var_total.set(total)


        
        elif(self.var_meal.get()=="lunch" and self.var_roomtype.get()=="luxury"):
            q1=float(600)
            q2=float(1000)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            tax="Rs."+str("%.2f"%((q5)*0.1))
            St="Rs."+str("%.2f"%((q5)))
            total="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(tax)
            self.var_actualtotal.set(St)
            self.var_total.set(total)






    









    





      



























































if __name__=="__main__":
    root=Tk()
    obj=room_book(root)
    root.mainloop()












































