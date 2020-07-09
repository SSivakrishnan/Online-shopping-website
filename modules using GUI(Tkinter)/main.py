from customer import *
from admin import *
import mysql.connector
from datetime import date,timedelta
from tkinter import *


cnx=mysql.connector.connect(user="root",database="online_shopping")
cursor=cnx.cursor(buffered=True)


root=Tk()
root.geometry('640x640+0+0')
root.title("")
root.configure(bg='#04042e')
x=IntVar()
x.set('admin')
lf=Frame(root,height=80,width=160,bg='#04042e')
lf.pack()
Label(lf,text='WELCOME TO ONLINE SHOPPING APP',font=('bold',40),fg='#67e9f0',bg='#04042e').grid()

def fun1(val,lf):
    if(val==0):#customer
        
        lf.destroy()
        cus=Customer(cursor,cnx,root)
    
        
        lfc=Frame(root,height=80,width=160,bg='#04042e')
        lfc.pack()
        def signn(vall):
            if(vall==22):#signin
                cus.customer_signin(lfc)
            elif(vall==11):#signup
                cus.customer_signup(lfc)
            #Label(lfc,text=vall).pack()
        y=IntVar()
        y.set('SIGN IN')
        signin=Radiobutton(lfc,text='SIGN IN',variable=y,value=22,font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
        signup=Radiobutton(lfc,text='SIGN OUT',variable=y,value=11,font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
        
        Button(lfc,text='Go next ->',command=lambda:signn(y.get()),bg='#080870',fg='#67e9f0',height=2,width=8,font=('bold',10)).pack()
        
    elif(val==1):#admin
        ad=Admin(cursor,cnx,root)
        ad.admin_signin(lf)
        

        

Label(lf,text='CHOOSE YOUR ROLE:',font=('bold',14),fg='#67e9f0',bg='#04042e').grid()
rb1=Radiobutton(lf,text="ADMIN",variable=x,value=1,bg='#04042e',font=('bold',18),fg='#67e9f0').grid()
rb2=Radiobutton(lf,text="CUSTOMER",variable=x,value=0,bg='#04042e',font=('bold',18),fg='#67e9f0').grid()
Button(lf,text='Go next ->',command=lambda:fun1(x.get(),lf),bg='#080870',fg='#67e9f0',height=2,width=8,font=('bold',10)).grid()


root.mainloop()