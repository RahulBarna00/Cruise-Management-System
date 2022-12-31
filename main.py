from tkinter import *
from PIL import Image,ImageTk
import mariadb
from tkcalendar import *
from tkinter import messagebox

tk = Tk()
tk.geometry('1280x720')
tk.title("Cruise Management System")
#tk.state('zoomed')

def wlcm():
       mainbac = Image.open('image\\main_menu.jpg')
       img1 =ImageTk.PhotoImage(mainbac)
       label = Label(tk, image=img1)
       label.place(x=0, y=0)
       
       #==============Admin Button==================
       adminbtn = Button(tk,text='Admin',bd='3',bg="Grey",fg="Black",height=1,width=10,command=admin).place(x=1180, y=660) 
       #============New User Button=================
       nusrbtn = Button(tk,text='New User',bd='3',bg="black",fg="White",height=2,width=30,command=new).place(x=950, y=140) 
       #=========Existing user button===============
       eusrbtn = Button(tk,text='Existing User',bg="black",fg="White",height=2,width=30,command=exist).place(x=950, y=200) 
       #==============Exit button===================
       exitbtn = Button(tk,text='Exit',bd='3',bg="black",fg="White",height=1,width=15,command = tk.destroy).place(x=1053, y=260)

       tk.mainloop()

def new():
       signbac = Image.open('image\\signup.jpg')
       img2 = ImageTk.PhotoImage(signbac)
       label = Label(tk,image=img2)
       label.place(x=0,y=0)

       global name1,name2,usr1,mobno1,pas1,paas2

       #===========Name============
       name = Label(tk ,text = "Name",height=1,width=14).place(x=780,y=160)
       name1 = Entry(tk)
       name1.place(x=910,y=160)

       name2 = Entry(tk)
       name2.place(x=1050,y=160)

       #=========Userid==========
       usr = Label(tk ,text = "User Id",height=1,width=14).place(x=780,y=190)
       usr1 = Entry(tk)
       usr1.place(x=910,y=190)

       #======Contact Number=======
       mobno = Label(tk ,text = "Contact Number",height=1,width=14).place(x=780,y=220)
       mobno1 = Entry(tk)
       mobno1.place(x=910,y=220)

       #========Password 1=========
       pas = Label(tk,text="Password",height=1,width=14).place(x=780,y=250)
       pas1 = Entry(tk,show="*")
       pas1.place(x=910,y=250)

       #======Password 2 Re========
       paas = Label(tk,text="Re-enter Password",height=1,width=14).place(x=780,y=280)
       paas2 = Entry(tk,show="*")
       paas2.place(x=910,y=280)

       #=========Sign Up===========
       sgnup = Button(tk,text="Sign Up",bd="2",bg="black",fg="white",height=1,width=34,command = new_login).place(x=780,y=320)
       #=======Exit button=========
       exitbtn = Button(tk,text='Exit',bd='2',bg="black",fg="White",height=1,width=16,command=tk.destroy).place(x=1040,y=320)
       #====Return To Main Menu====
       back = Button(tk,bd="3",bg="black",fg="white",text="Return To Main Menu",height=1,width=20,command=wlcm).place(x=1080,y=640)

       tk.mainloop()

def exist():
       logbac = Image.open('image\\login.jpg')
       img3 = ImageTk.PhotoImage(logbac)
       label = Label(tk,image=img3)
       label.place(x=0,y=0)

       global usrentr,pasentr

       username = StringVar()
       password = StringVar()

       #=======Username========
       userlab = Label(tk,text="Username",height=1,width=10).place(x=865,y=160)
       usrentr = Entry(textvariable=username)
       usrentr.place(x=960,y=160)
       #=======Password========
       passlab = Label(tk,text="Password",height=1,width=10).place(x=865,y=200)
       pasentr = Entry(textvariable=password,show="*")
       pasentr.place(x=960,y=200)
       #=====Login Button======
       logn = Button(tk,bd="3",bg="grey",fg="white",text="Login",height=1,width=16,command=exist_login).place(x=960,y=240)
       #======Exit Button======
       exitbtn = Button(tk,text='Exit',bd='3',bg="black",fg="White",height=1,width=10,command=tk.destroy).place(x=865, y=240)
       #===Create New Button===
       newacc = Button(tk,text="Create New Account",bd="3",bg="White",fg="black",height=1,width=30,command=new).place(x=865,y=280) 
       #==Return To Main Menu==
       back = Button(tk,bd="3",bg="black",fg="white",text="Return To Main Menu",height=1,width=20,command=wlcm).place(x=1080,y=640)

       tk.mainloop()

def admin():
       adm = Image.open('image\\admin.jpg')
       img4 = ImageTk.PhotoImage(adm)
       label = Label(tk,image=img4)
       label.place(x=0,y=0)

       global usrentr,pasentr

       userid = StringVar()
       passid = StringVar()
       #=======Username========

       userlab = Label(tk,text="Username",height=1,width=10).place(x=975,y=200)
       usrentr = Entry(textvariable=userid)
       usrentr.place(x=1070,y=200)

       #=======Password========
       passlab = Label(tk,text="Password",height=1,width=10).place(x=975,y=240)
       pasentr = Entry(textvariable=passid,show="*")
       pasentr.place(x=1070,y=240)
        
       #=====Login Button======
       logn = Button(tk,bd="3",bg="grey",fg="white",text="Login",height=1,width=16,command=admin_login).place(x=1070,y=280)
       #======Exit Button======
       exitbtn = Button(tk,text='Exit',bd='3',bg="black",fg="White",height=1,width=10,command=tk.destroy).place(x=975, y=280)
       #==Return To Main Menu==
       back = Button(tk,bd="3",bg="black",fg="white",text="Return To Main Menu",height=1,width=20,command=wlcm).place(x=1080,y=640)

       tk.mainloop()

def adminpage():
       adminpage = Image.open('image\\adminpage.jpg')
       lastpage =ImageTk.PhotoImage(adminpage)
       label = Label(tk, image=lastpage)
       label.place(x=0, y=0)

       mydb = mariadb.connect(host="127.0.0.1",user="root",passwd="",database="cruisems")
       mycursor = mydb.cursor()

       #=========Userid==========
       username = StringVar(tk,value="Enter Username")
       Label(tk ,text = "Username",height=1,width=14).place(x=275,y=450)

       usernme = Entry(tk,textvariable=username)
       usernme.place(x=390,y=451)

       labelFrame = Frame(tk,bg='black')
       labelFrame.place(relx=0.2,rely=0.85,relwidth=0.1,relheight=0.1)
       y = 0.25

       labelFrame2 = Frame(tk,bg='black')
       labelFrame2.place(relx=0.3,rely=0.85,relwidth=0.1,relheight=0.1)
       y = 0.25

       labelFrame3 = Frame(tk,bg='black')
       labelFrame3.place(relx=0.4,rely=0.85,relwidth=0.1,relheight=0.1)
       y = 0.25

       labelFrame4 = Frame(tk,bg='black')
       labelFrame4.place(relx=0.5,rely=0.85,relwidth=0.1,relheight=0.1)
       y = 0.25

       labelFrame5 = Frame(tk,bg='black')
       labelFrame5.place(relx=0.6,rely=0.85,relwidth=0.1,relheight=0.1)
       y = 0.25

       labelFrame6 = Frame(tk,bg='black')
       labelFrame6.place(relx=0.7,rely=0.85,relwidth=0.1,relheight=0.1)
       y = 0.25

       labelFrame7 = Frame(tk,bg='black')
       labelFrame7.place(relx=0.8,rely=0.85,relwidth=0.1,relheight=0.1)
       y = 0.25

       def check():
              labelFrame = Frame(tk,bg='black')
              labelFrame.place(relx=0.2,rely=0.85,relwidth=0.1,relheight=0.1)
              y = 0.25

              labelFrame2 = Frame(tk,bg='black')
              labelFrame2.place(relx=0.3,rely=0.85,relwidth=0.1,relheight=0.1)
              y = 0.25

              labelFrame3 = Frame(tk,bg='black')
              labelFrame3.place(relx=0.4,rely=0.85,relwidth=0.1,relheight=0.1)
              y = 0.25

              labelFrame4 = Frame(tk,bg='black')
              labelFrame4.place(relx=0.5,rely=0.85,relwidth=0.1,relheight=0.1)
              y = 0.25

              labelFrame5 = Frame(tk,bg='black')
              labelFrame5.place(relx=0.6,rely=0.85,relwidth=0.1,relheight=0.1)
              y = 0.25

              labelFrame6 = Frame(tk,bg='black')
              labelFrame6.place(relx=0.7,rely=0.85,relwidth=0.1,relheight=0.1)
              y = 0.25

              labelFrame7 = Frame(tk,bg='black')
              labelFrame7.place(relx=0.8,rely=0.85,relwidth=0.1,relheight=0.1)
              y = 0.25
              quer0 = "select * from personalinfo where usrid = %s and usrid = %s"
              quer01 = (usernme.get(),usernme.get())
              mycursor.execute(quer0,quer01)
              
              for i in mycursor:
                     Label(labelFrame, text="%-10s"%(i[0]),bg='black',fg='white').place(relx=0.07,rely=0.1)
                     Label(labelFrame2, text="%-20s"%(i[1]),bg='black',fg='white').place(relx=0.07,rely=0.1)
                     Label(labelFrame3, text="%-30s"%(i[4]),bg='black',fg='white').place(relx=0.07,rely=0.1)
                     Label(labelFrame4, text="%-40s"%(i[3]),bg='black',fg='white').place(relx=0.07,rely=0.1)

              try:
                     query = "select * from customer where usrid = %s and usrid = %s"
                     quer1 = (usernme.get(),usernme.get())
                     mycursor.execute(query,quer1)

                     for j in mycursor:
                            Label(labelFrame5, text="%-50s"%(j[0]),bg='black',fg='white').place(relx=0.07,rely=0.1)
                            Label(labelFrame6, text="%-60s"%(j[1]),bg='black',fg='white').place(relx=0.07,rely=0.1)
                            Label(labelFrame7, text="%-70s"%(j[2]),bg='black',fg='white').place(relx=0.07,rely=0.1)

              except:
                     for i in range(0,3+1): 
                            Label(labelFrame5, text="No Record",bg='black',fg='white').place(relx=0.07,rely=0.1)
                            Label(labelFrame6, text="No Record",bg='black',fg='white').place(relx=0.07,rely=0.1)
                            Label(labelFrame7, text="No Record",bg='black',fg='white').place(relx=0.07,rely=0.1)

       checkbtn = Button(tk,text="Ok",bd="2",bg="black",fg="white",width=15,command=check).place(x=400,y=490)
        
       tk.mainloop()    

def admin_login():
       mydb = mariadb.connect(host="127.0.0.1",user="root",passwd="",database="cruisems")
       mycursor = mydb.cursor()

       usrid = usrentr.get()
       pasid = pasentr.get()

       query = "select username,password from admin where username = %s and password = %s"
       query2 = (usrid,pasid)

       mycursor.execute(query,query2)
       res = mycursor.fetchall()

       count = mycursor.rowcount

       if count > 0:
        mycursor.close()
        messagebox.showinfo("Sucess","Login Successfully")
        adminpage()
       else:
        messagebox.showinfo("Try Again","Invalid Password")

def new_login():
    mydb = mariadb.connect(host="127.0.0.1",user="root",passwd="",database="cruisems")
    mycursor = mydb.cursor()

    global usrid
    
    fname = name1.get()
    lname = name2.get()
    usrid = usr1.get()
    mobileno = mobno1.get()
    temppass1 = pas1.get()
    temppass2 = paas2.get()
    
    if temppass1 == temppass2:
        password = temppass1
    else:
        messagebox.showinfo("Try Again","Please Check Both Entered Password")
    
    query = "insert into personalinfo(first_name,lastname,password,mobno,usrid) values(%s,%s,%s,%s,%s)"
    query2 = (fname,lname,password,mobileno,usrid)
    
    mycursor.execute(query,query2)
    mydb.commit()
    count = mycursor.rowcount
    
    if count > 0:
        mycursor.close()
        messagebox.showinfo("Sucess","Registered Successfully")
        main()
    else:
        messagebox.showinfo("Try Again","Invalid Password")

def exist_login():    
    mydb = mariadb.connect(host="127.0.0.1",user="root",passwd="",database="cruisems")
    mycursor = mydb.cursor()

    global usrid,pasid
    
    usrid = usrentr.get()
    pasid = pasentr.get()
    
    query = "select usrid,password from personalinfo where usrid = %s and password = %s"
    query2 = (usrid,pasid)
    
    mycursor.execute(query,query2)
    res = mycursor.fetchall()
    
    count = mycursor.rowcount
    
    if count > 0:
        mycursor.close()
        messagebox.showinfo("Sucess","Login Successfully")
        main()
    else:
        messagebox.showinfo("Try Again","Invalid Password")

def explore():
       exp = Image.open('image\\explore.jpg')
       img6 = ImageTk.PhotoImage(exp)
       label = Label(tk,image=img6)
       label.place(x=0,y=0)

       mydb = mariadb.connect(host="127.0.0.1",user="root",passwd="",database="cruisems")
       mycursor = mydb.cursor()

       #Boarding Point
       bop = StringVar()
       bop.set("Mumbai")
       mumbai = OptionMenu(tk , bop ,"Mumbai").place(x=400,y=150)

       #destination
       des = StringVar()
       des.set("Select Destination")
       places = OptionMenu(tk ,des,"NewYork","Miami","Dubai","HongKong","UAE","London")
       places.place(x=400,y=230)

       #no of person
       mem = StringVar()
       mem.set("Select No of members")
       values = OptionMenu(tk,mem,1,2,3,4,5,6,7,8,9)
       values.place(x=400,y=300)

       cal = DateEntry(tk, width=12, background='darkblue',foreground='white', borderwidth=3)
       cal.place(x=400,y=370)

       labelFrame = Frame(tk,bg='black')
       labelFrame.place(relx=0.6,rely=0.2,relwidth=0.1,relheight=0.4)
       y = 0.25

       labelFrame2 = Frame(tk,bg='black')
       labelFrame2.place(relx=0.68,rely=0.2,relwidth=0.1,relheight=0.4)
       y = 0.25
 
       labelFrame3 = Frame(tk,bg='black')
       labelFrame3.place(relx=0.76,rely=0.2,relwidth=0.1,relheight=0.4)
       y = 0.25

       Label(labelFrame, text="%-10s"%('Destination'),bg='black',fg='white').place(relx=0.07,rely=0.1)
       Label(labelFrame2, text="%-20s"%('Departure Time'),bg='black',fg='white').place(relx=0.07,rely=0.1)
       Label(labelFrame3, text="%-30s"%('Amount'),bg='black',fg='white').place(relx=0.07,rely=0.1)

       Label(labelFrame, text="------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
       Label(labelFrame2, text="------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
       Label(labelFrame3, text="--------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)

       try:
        mycursor.execute("select * from booking")
        mydb.commit()

        for i in mycursor:
            Label(labelFrame, text="%-10s"%(i[0]),bg='black',fg='white').place(relx=0.07,rely=y)
            Label(labelFrame2, text="%-20s"%(i[2]),bg='black',fg='white').place(relx=0.07,rely=y)
            Label(labelFrame3, text="%-30s"%(i[1]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
       except:
        messagebox.showinfo("Failed to fetch files from database")

       def confirmbkng():
        a = des.get()
        b = cal.get_date()
        c = mem.get()
        d = usrid

        query5 = "select amount*%s from booking where destination = %s"
        query6 = (c,a)
        
        mycursor.execute(query5,query6)
        amt = mycursor.fetchone()
        
        amt = amt[0]
        
        if des.get() == "Select Destination":
            messagebox.showinfo("Try Again","Please Select Your Destination")
        
        elif mem.get() == "Select Enter No of members":
            messagebox.showinfo("Try Again","Please No Of Members")

        else:
            MsgBox = messagebox.askquestion('Confirm','Confirm Booking?')

            if MsgBox == 'yes':
                query3 = "insert into customer(destination,dtedep,noppl,usrid,ttlamt) values(%s,%s,%s,%s,%s)"
                query4 = (a,b,c,d,amt)
                
                mycursor.execute(query3,query4)
                mydb.commit()
                

                messagebox.showinfo('Confirmed','Thank You For Booking')

       okbtn = Button(tk, text="Confirm Booking",command=confirmbkng)
       okbtn.place(x=400,y=600)

       back = Button(tk,bd="3",bg="black",fg="white",text="Back",height=1,width=10,command=main).place(x=1140,y=640)

       tk.mainloop()

def tdetail():
    tde = Image.open('image\\tdetail.jpg')
    img8 = ImageTk.PhotoImage(tde)
    label = Label(tk,image=img8)
    label.place(x=0,y=0)

    try:
        mydb = mariadb.connect(host="127.0.0.1",user="root",passwd="",database="cruisems")
        mycursor = mydb.cursor()

        query00 = "select destination from customer where usrid = usrid"
        mycursor.execute(query00)
        for i in mycursor:
            dest = i[0]

        destin = str(dest)
        
        lasquery = 'select detime from booking where destination = %s or destination = %s'
        lasquery2= (destin,dest)
        mycursor.execute(lasquery,lasquery2)

        for i in mycursor:
            deptm = i[0]

        query0 = "select * from customer where usrid = %s and destination = %s"
        query001 = (usrid,dest)

        mycursor.execute(query0,query001)
        for i in mycursor:
            tmem = i[0]
            djor = i[2]
            amount = i[3]

        labelFrame = Frame(tk,bg='black')
        labelFrame.place(x=300,y=76 ,relwidth=0.31,relheight=0.6)

        label0 = Label(tk,bg='black',fg='White',text='Cruise Management System',font = ('Bold', 20)).place(x=320,y=80)
               
        label = Label(tk,bg='black',fg='White',text='Latest Travel Detail',font=('Bold', 20)).place(x=370,y=120)
        
        label1 = Label(tk,bg='black',fg='White',text='From',font=('Bold',14)).place(x=320,y=170)
        val1 = Label(tk,bg="Black",fg="White",text="Mumbai",font=('Bold',14)).place(x=600,y=170)
        
        
        label2 = Label(tk,bg='black',fg='White',text='Destination',font=('Bold',14)).place(x=320,y=220)
        val2 = Label(tk,bg="Black",fg="White",text=dest,font=('Bold',14)).place(x=600,y=220)
        
        label3 = Label(tk,bg='black',fg='White',text='Departure Time',font=('Bold',14)).place(x=320,y=270)
        val3 = Label(tk,bg="Black",fg="White",text=deptm,font=('Bold',14)).place(x=600,y=270)

        label4 = Label(tk,bg='black',fg='White',text='Date Of Journey',font=('Bold',14)).place(x=320,y=320)
        val4 = Label(tk,bg="Black",fg="White",text=djor,font=('Bold',14)).place(x=600,y=310)

        label6 = Label(tk,bg='black',fg='White',text='Total Members',font=('Bold',14)).place(x=320,y=370)
        val6 = Label(tk,bg="Black",fg="White",text=tmem,font=('Bold',14)).place(x=600,y=370)
        
        label5 = Label(tk,bg='black',fg='White',text='Total Amount',font=('Bold',14)).place(x=320,y=420)
        val5 = Label(tk,bg="Black",fg="White",text=amount,font=('Bold',14)).place(x=600,y=420)

        def cancel():
               mydb = mariadb.connect(host="127.0.0.1",user="root",passwd="",database="cruisems")
               mycursor = mydb.cursor()

               quey0 = "delete from customer where usrid = %s and usrid = %s"
               quer0 = (usrid,usrid)

               ask1 = messagebox.askquestion("Confirm","Confirm Cancel Tickets")
               
               if ask1 == "yes":
                      mycursor.execute(quey0,quer0)
                      mydb.commit()

                      if mycursor.rowcount > 0:
                             messagebox.showinfo("Sucess","Sucesfully cancelled")
                      else:
                             messagebox.showinfo("Try Again","Failed to Cancel Tickets")
               else:
                      pass
        Cancel = Button(tk,bd="3",bg = "White",fg="Black",text="Cancel Ticket",height=2,width=15,command=cancel).place(x=600,y=500)

        back = Button(tk,bd="3",bg="black",fg="white",text="Back",height=1,width=10,command=main).place(x=1140,y=640)
    except:
        messagebox.showinfo("Invalid","You don't have any active booking")
        main()

    tk.mainloop()

def update():
       mydb = mariadb.connect(host="127.0.0.1",user="root",passwd="",database="cruisems")
       mycursor = mydb.cursor()

       if paas2.get() == pas1.get():
        global passwor
        passwor = pas1.get()
        
        query = "update personalinfo set first_name = %s,lastname = %s,mobno = %s,usrid = %s,password = %s where usrid = %s"
        query2 = (name1.get(),name2.get(),mob1.get(),usr1.get(),passwor,usrid)

        mycursor.execute(query,query2)
        mydb.commit()
        
        messagebox.showinfo("Sucess","  Sucesfully Updated!\nReturning To Login Page.")
        exist()
       else:
        messagebox.showinfo("Error","Please Check Both Passowrd!")
        
def pinfo():
       pinf = Image.open('image\\pinfo.jpg')
       img9 = ImageTk.PhotoImage(pinf)
       label = Label(tk,image=img9)
       label.place(x=0,y=0)

       mydb = mariadb.connect(host="127.0.0.1",user="root",passwd="",database="cruisems")
       mycursor = mydb.cursor()

       inquery = "select * from personalinfo where usrid = %s and password = %s"
       inquery2 = (usrid,pasid)

       mycursor.execute(inquery,inquery2)
       result = mycursor.fetchone()

       global fname,lname,passw,mobno,usern
       global name1,name2,usr1,mob1,pas1,paas2

       fname = result[0]
       lname = result[1]
       passw = result[2]
       mobno = result[3]
       usern = result[4]

       namevar = StringVar(tk,value=fname)
       #===========Name============
       name = Label(tk ,text = "Name",height=1,width=14).place(x=780,y=160)
       name1 = Entry(tk,textvariable=namevar)
       name1.place(x=910,y=160)

       lanamevr = StringVar(tk,value=lname)
       name2 = Entry(tk,textvariable=lanamevr)
       name2.place(x=1050,y=160)

       uservar = StringVar(tk,value=usern)
       #=========Userid==========
       usr = Label(tk ,text = "User Id",height=1,width=14).place(x=780,y=190)
       usr1 = Entry(tk,textvariable=uservar)
       usr1.place(x=910,y=190)

       mobvar = StringVar(tk,value=mobno)
       #======Contact Number=======
       mob = Label(tk ,text = "Contact Number",height=1,width=14).place(x=780,y=220)
       mob1 = Entry(tk,textvariable=mobvar)
       mob1.place(x=910,y=220)

       pasvar = StringVar(tk,value=passw)
       #========Password 1=========
       pas = Label(tk,text="Password",height=1,width=14).place(x=780,y=250)
       pas1 = Entry(tk,show="*",textvariable=pasvar)
       pas1.place(x=910,y=250)

       pasvar2 = StringVar(tk,value=passw)
       #======Password 2 Re========
       paas = Label(tk,text="Re-enter Password",height=1,width=14).place(x=780,y=280)
       paas2 = Entry(tk,show="*",textvariable=pasvar2)
       paas2.place(x=910,y=280)

       updatebtn = Button(tk,text="Ok",bd="2",bg="black",fg="white",height=1,width=34,command=update).place(x=780,y=320)

       back = Button(tk,bd="3",bg="black",fg="white",text="Back",height=1,width=10,command=main).place(x=1140,y=640)
        
       tk.mainloop()

def lgout():
       msgbx = messagebox.askquestion("Confirm","Are You Sure?")
       if msgbx == 'yes':
        messagebox.showinfo("Success","Logged Out")
        tk.destroy()
       else:
        pass

def main():
       mn = Image.open('image\\mainwlcm.jpg')
       img5 = ImageTk.PhotoImage(mn)
       label = Label(tk,image=img5)
       label.place(x=0,y=0)

       Explore = Button(tk,text='Explore',bd='5',bg="#ECF0F1",fg="black",height=3,width=24,command=explore).place(x=50, y=220) 

       Tdetail = Button(tk,text='Travel Details',bd='5',bg="#ECF0F1",fg="Black",height=3,width=24,command=tdetail).place(x=50, y=325)

       Pinfo = Button(tk,text='Personal Information',bd='5',bg="#ECF0F1",fg="Black",height=3,width=24,command=pinfo).place(x=50, y=430)

       Logout = Button(tk,text='Logout',bd='4',bg="#ECF0F1",fg="Black",height=3,width=24,command=lgout).place(x=50, y=610)

       tk.mainloop()

wlcm()
