from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
from tkinter import messagebox
import mysql.connector

class cust_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")



        #================variables====================
        self.var_ref=StringVar()
        x=random.randint(1000,10000)
        self.var_ref.set(str(x))

        self.var_custname=StringVar()
        self.var_mothername=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()






        # --------------title--------------
        lbl_title=Label(self.root,text="Add Customer Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

         # ----------------logo--------------
        img2=Image.open(r"C:\Users\admin\Desktop\SE PRJ\photos\vecteezy_vector-illustration-logo-grand-hotel-boutique-vintage-design_13087536.jpg")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)


        # -------------------label frame----------------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="customer details",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        #------------------labels and entrys-----------------------------
        lbl_cust_ref=Label(labelframeleft,text="customer reference : ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="read only")
        entry_ref.grid(row=0,column=1)

        #cust name
        cname=Label(labelframeleft,text="customer name : ",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_custname,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        #mother name
        lblmname=Label(labelframeleft,text="mother name : ",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mothername,width=29,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)

        #gender combobox
        lbl_gender=Label(labelframeleft,font=("arial",12,"bold"),text="gender : ",padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="read only")
        combo_gender["value"]=("Male","Female")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        

        #postcode
        lblpsotcode=Label(labelframeleft,text="postcode : ",font=("arial",12,"bold"),padx=2,pady=6)
        lblpsotcode.grid(row=4,column=0,sticky=W)
        txtpdcode=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("arial",13,"bold"),width=29)
        txtpdcode.grid(row=4,column=1)


        #mobilenummber
        lblmobile=Label(labelframeleft,text="mobile : ",font=("arial",12,"bold"),padx=2,pady=6)
        lblmobile.grid(row=5,column=0,sticky=W)
        txtmno=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
        txtmno.grid(row=5,column=1)


        #email
        lblemaill=Label(labelframeleft,text="email : ",font=("arial",12,"bold"),padx=2,pady=6)
        lblemaill.grid(row=6,column=0,sticky=W)
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        txtemail.grid(row=6,column=1)


        #nationality
        lblnationality=Label(labelframeleft,text="natinality : ",font=("arial",12,"bold"),padx=2,pady=6)
        lblnationality.grid(row=7,column=0,sticky=W)
        combo_nation=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="read only")
        combo_nation["value"]=("indian","american")
        combo_nation.current(0)
        combo_nation.grid(row=7,column=1)


        #idproof type combobox
        lblidproof=Label(labelframeleft,text="id proof type : ",font=("arial",12,"bold"),padx=2,pady=6)
        lblidproof.grid(row=8,column=0,sticky=W)
        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="read only")
        combo_id["value"]=("Aadhar card","Pan card")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)



        #id number
        lblidnumber=Label(labelframeleft,text="id number : ",font=("arial",12,"bold"),padx=2,pady=6)
        lblidnumber.grid(row=9,column=0,sticky=W)
        txtid=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=29)
        txtid.grid(row=9,column=1)



        #address
        lbladd=Label(labelframeleft,text="address : ",font=("arial",12,"bold"),padx=2,pady=6)
        lbladd.grid(row=10,column=0,sticky=W)
        txtadd=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=29)
        txtadd.grid(row=10,column=1)



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



        #--------------table frame search system---------------
        table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="view details and search system",font=("times new roman",12,"bold"),padx=2)
        table_frame.place(x=435,y=50,width=860,height=490)

        lblsearchby=Label(table_frame,text="search by : ",font=("arial",12,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="read only")
        combo_search["value"]=("Mobile","ref")
        combo_id.current(0)
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
        detail_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_Y=ttk.Scrollbar(detail_table,orient=VERTICAL)


        self.cust=ttk.Treeview(detail_table,column=("ref","name",'mother name','gender','postcode','mobile','email','nationality','idproof','idnumber','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_Y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_Y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust.xview)
        scroll_Y.config(command=self.cust.yview)



        self.cust.heading("ref",text="refer no")
        self.cust.heading("name",text="Name")
        self.cust.heading("mother name",text="Mother name")
        self.cust.heading("gender",text="Gender")
        self.cust.heading("postcode",text="postalcode")
        self.cust.heading("mobile",text="mobile no")
        self.cust.heading("email",text="Email")
        self.cust.heading("nationality",text="Nationanlity")
        self.cust.heading("idproof",text="Id proof")
        self.cust.heading("idnumber",text="Id number")
        self.cust.heading("address",text="Address")

        self.cust["show"]='headings'
        self.cust.column("ref",width=100)
        self.cust.column("name",width=100)
        self.cust.column("mother name",width=100)
        self.cust.column("gender",width=100)
        self.cust.column("postcode",width=100)
        self.cust.column("mobile",width=100)
        self.cust.column("email",width=100)
        self.cust.column("nationality",width=100)
        self.cust.column("idproof",width=100)
        self.cust.column("idnumber",width=100)
        self.cust.column("address",width=100)
        self.cust.pack(fill=BOTH,expand=1)
        self.cust.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mothername.get()=="":
            messagebox.showerror("error","all fields are required",parent=self.root)
        else:
            try:  
                conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
                my_cursor=conn.cursor()
                print("INSERT INTO customer2 VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" %(
                                                                                    self.var_ref.get(),
                                                                                    self.var_custname.get(),
                                                                                    self.var_mothername.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_post.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_id_proof.get(),
                                                                                    self.var_id_number.get(),
                                                                                    self.var_address.get()
                                                                                ))
                my_cursor.execute("INSERT INTO customer2 VALUE (%s,'%s','%s','%s',%s,'%s','%s','%s','%s','%s','%s')" %(
                                                                                    self.var_ref.get(),
                                                                                    self.var_custname.get(),
                                                                                    self.var_mothername.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_post.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_id_proof.get(),
                                                                                    self.var_id_number.get(),
                                                                                    self.var_address.get()
                                                                                ))
                conn.commit()
                i=[self.var_ref.get(),self.var_custname.get(),self.var_mothername.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_post.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_id_proof.get(),
                                                                                    self.var_id_number.get(),
                                                                                    self.var_address.get()]
                self.cust.insert("",END,values=i)
                conn.close()
                messagebox.showinfo("success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong : {str(es)}",parent=self.root)

    def fetch_data(self):
        try:
            for item in self.cust.get_children():
                self.cust.delete(item)
        except:
            pass
        conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer2")
        rows=my_cursor.fetchall()
        if len(rows)!=0:

            for i in rows:
                self.cust.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.cust.focus()
        content=self.cust.item(cursor_row)
        row=content["values"]
        print(row)

        self.var_ref.set(row[0])
        self.var_custname.set(row[1])
        self.var_mothername.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])


    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("error","please enter mobile number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer2 set custname='%s',mothername='%s',gender='%s',postcode=%s,mobile='%s',email='%s',nationality='%s',idproof='%s',id_number='%s',address='%s' where ref=%s" %(
                                                                                                                                                                                self.var_custname.get(),
                                                                                                                                                                                self.var_mothername.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_post.get(),
                                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_nationality.get(),
                                                                                                                                                                                self.var_id_proof.get(),
                                                                                                                                                                                self.var_id_number.get(),
                                                                                                                                                                                self.var_address.get(),  
                                                                                                                                                                                self.var_ref.get()                                                                                                                                                    
                                                                                                                                                                            ))
            conn.commit()
            conn.close()
            messagebox.showinfo("update","customer details has been added succesfully",parent=self.root)
            i=[self.var_ref.get(),self.var_custname.get(),self.var_mothername.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_post.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_id_proof.get(),
                                                                                    self.var_id_number.get(),
                                                                                    self.var_address.get()]
            self.cust.insert("",END,values=i)                                            
            selected_item = self.cust.selection()[0]
            self.cust.delete(selected_item)

    def delete(self):
        delete=messagebox.askyesno("hotel management system","do you want delete this customer",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
            my_cursor=conn.cursor()
            query="delete from customer2 where ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
            selected_item = self.cust.selection()[0]
            self.cust.delete(selected_item)
            messagebox.showinfo("update","customer details has been deleted succesfully",parent=self.root)
        else:
            if not delete:
                return
        conn.commit()      
        conn.close()

    def reset(self):    #to fix the values of combobox we comment out them
        #self.var_ref.set("")
        self.var_custname.set("")
        self.var_mothername.set("")
        #self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        #self.var_nationality.set("")
        #self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")
        x=random.randint(1000,10000)
        self.var_ref.set(str(x))
    

    def search(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="vipul",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer2 where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            for item in self.cust.get_children():
                self.cust.delete(item)
            for i in rows:
                self.cust.insert("",END,values=i)
            conn.commit()
        conn.close()
            


if __name__=="__main__":
    root=Tk()
    obj=cust_window(root)
    root.mainloop()




