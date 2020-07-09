from datetime import date,timedelta
from tkinter import *
from tkinter import messagebox

from time import strftime
class Customer:
    def __init__(self,cursor,cnx,root):
        self.cursor=cursor
        self.cnx=cnx
        self.root=root
    def customer_signup(self,lfc):
        lfc.destroy()
        lfcsu=Frame(self.root,height=80,width=160,bg='#04042e')
        lfcsu.pack()

        Label(lfcsu,text='CUSTOMER',font=('bold',35),fg='#67e9f0',bg='#04042e').grid()
        Label(lfcsu,text='SIGNUP PAGE',font=('bold',25),fg='#67e9f0',bg='#04042e').grid()
        Label(lfcsu,text='Enter your id:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=2,column=0)
        Label(lfcsu,text='Enter your name:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=3,column=0)
        Label(lfcsu,text='Enter your phone number:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=4,column=0)
        Label(lfcsu,text='Enter the password',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=5,column=0)
        Label(lfcsu,text='Enter your address:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=6,column=0)


        cus_id=Entry(lfcsu,bg='#02021c',fg='#67e9f0')
        name=Entry(lfcsu,bg='#02021c',fg='#67e9f0')
        phone_no=Entry(lfcsu,bg='#02021c',fg='#67e9f0')
        password=Entry(lfcsu,bg='#02021c',fg='#67e9f0')
        address=Entry(lfcsu,bg='#02021c',fg='#67e9f0')
        cus_id.grid(row=2,column=1)
        name.grid(row=3,column=1)
        phone_no.grid(row=4,column=1)
        password.grid(row=5,column=1)
        address.grid(row=6,column=1)
        
        def submit():
            query="INSERT INTO customer(cus_id,name,phone_no,password,address) VALUES( %s, %s, %s,%s,%s)"
            self.cursor.execute(query,(cus_id.get(),name.get(),phone_no.get(),password.get(),address.get()))
            self.cnx.commit()
            self.customer_home(cus_id,address,lfcsu)
        Button(lfcsu,text='Submit',command=submit,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).grid(row=6,column=0)

        
    def customer_signin(self,lfc):
        lfc.destroy()
        lfcsi=Frame(self.root,height=80,width=160,bg='#04042e')
        lfcsi.pack()
        Label(lfcsi,text='SIGNIN PAGE',font=('bold',25),fg='#67e9f0',bg='#04042e').grid()
        Label(lfcsi,text='Enter your name:',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=1,column=0)
        Label(lfcsi,text='Enter the password',font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=2,column=0)
        name=Entry(lfcsi,bg='#02021c',fg='#67e9f0')
        password=Entry(lfcsi,bg='#02021c',fg='#67e9f0')
        name.grid(row=1,column=1)
        password.grid(row=2,column=1)
        def submit():
            query="SELECT name,password FROM customer WHERE name=%s and password=%s"
            self.cursor.execute(query,(name.get(),password.get()))
            val=self.cursor.fetchone()

            query="SELECT cus_id FROM customer WHERE name=%s and password=%s"
            self.cursor.execute(query,(name.get(),password.get()))
            cus=self.cursor.fetchone()
            cus_id=cus[0]

            query="SELECT address FROM customer WHERE name=%s and password=%s"
            self.cursor.execute(query,(name.get(),password.get()))
            addd=self.cursor.fetchone()
            address=addd[0]

            if(val==None):
                messagebox.showinfo('Unsuccessful signin','please Enter valid username and password')
            else:
                self.customer_home(cus_id,address,lfcsi)

        
        Button(lfcsi,text='Submit',command=submit,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).grid(row=6,column=0)
        
        

    def customer_home(self,cus_id,address,prev):
        
        prev.destroy()
        lfch=Frame(self.root,height=80,width=160,bg='#04042e')
        lfch.pack()
       
        def search_item():
            lfch.destroy()
         
            
            lfcst=Frame(self.root,height=80,width=160,bg='#04042e')
            lfcst.pack()
            l1=Label(lfcst,text="Enter the item:",font=('bold',18),fg='#67e9f0',bg='#04042e')
            l1.grid(row=0,column=0)

            item=Entry(lfcst,bg='#02021c',fg='#67e9f0')
            item.grid(row=0,column=1)
            def search(item):
                lfcst.destroy()
                lfcsts=Frame(self.root,height=80,width=160,bg='#04042e')
                lfcsts.pack()
                #global lfcsts
                query="SELECT item_id,item_name,price,specification,quantity FROM product WHERE item_name=%s and item_name=%s"
                self.cursor.execute(query,(item,item))
                i=self.cursor.fetchone()
                item_id,item_name,price,specification,quantity=i
                i2=Label(lfcsts,text='{}-{}-{}-{}-{}'.format(item_id,item_name,price,specification,quantity),font=('bold',12),fg='#67e9f0',bg='#04042e')
                i2.pack()
        
                def buy():
                    lfcsts.destroy()
                    lfcstsb=Frame(self.root,height=80,width=160,bg='#04042e')
                    lfcstsb.pack()
                    Label(lfcstsb,text="Available quantity::{}".format(quantity),font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=0,column=0)
                    self.customer_buy(item_id,cus_id,address,lfcstsb)
                def addtocart():
                    lfcsts.destroy()
                    lfcstsc=Frame(self.root,height=80,width=160,bg='#04042e')
                    lfcstsc.pack()
                    self.customer_add_to_cart(item_id,cus_id,address,lfcstsc)
                def back():
                    self.customer_home(cus_id,address,lfcsts)

                b2=Button(lfcsts,text='Buy',command=buy,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b2.pack()
                b3=Button(lfcsts,text='Add to cart',command=addtocart,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b3.pack()
                b4=Button(lfcsts,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b4.pack()
            def back():
                    self.customer_home(cus_id,address,lfcst)



            b1=Button(lfcst,text='Search',command=lambda:search(item.get()),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
            b1.grid()
            b10=Button(lfcst,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
            b10.grid()


            
        def display_item():
            lfch.destroy()
            lfcdt=Frame(self.root,height=80,width=160,bg='#04042e')
            lfcdt.pack()
            Label(lfcdt,text='search item',font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
            lib1=Listbox(lfcdt)
            lib1.pack(pady=20,padx=30)
            query="SELECT item_id,item_name,price FROM product"
            self.cursor.execute(query)
            lst1=self.cursor.fetchall()   
            for item in lst1:
                a,b,c=item
                lib1.insert(END,'>{} - Rs.{} - {}'.format(b,c,a)) 
            def select(lib1,lfcdt):
                lfcdt.destroy()
                lfcdtd=Frame(self.root,height=80,width=160,bg='#04042e')
                lfcdtd.pack()
                lii1=lib1
                lii=lii1.split('-')
                i_id=lii[2].strip()
                query="SELECT item_name,specification,quantity FROM product WHERE item_id=%s and item_id=%s"
                self.cursor.execute(query,(i_id,i_id))
                lst2=self.cursor.fetchone()
                a,b,quantity=lst2
                Label(lfcdtd,text="Product name:{}".format(a),font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
                Label(lfcdtd,text="Specification:{}".format(b),font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
                def buy():
                    lfcdtd.destroy()
                    lfcdtdb=Frame(self.root,height=80,width=160,bg='#04042e')
                    lfcdtdb.pack()
                    Label(lfcdtdb,text="Available quantity::{}".format(quantity),font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=0,column=0)
                    self.customer_buy(i_id,cus_id,address,lfcdtdb)
                def addtocart():
                    lfcdtd.destroy()
                    lfcdtdc=Frame(self.root,height=80,width=160,bg='#04042e')
                    lfcdtdc.pack()
                    self.customer_add_to_cart(i_id,cus_id,address,lfcdtdc)
                def back():
                    self.customer_home(cus_id,address,lfcdtd)

                b2=Button(lfcdtd,text='Buy',command=buy,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b2.pack()
                b3=Button(lfcdtd,text='Add to cart',command=addtocart,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b3.pack()
                b4=Button(lfcdtd,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b4.pack()
            def back():
                    self.customer_home(cus_id,address,lfcdt)


            Button(lfcdt,text='Select',command=lambda:select(lib1.get(ANCHOR),lfcdt),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            Button(lfcdt,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            
            
            
            
           

        def cart():
            lfch.destroy()
            lfch_c=Frame(self.root,bg='#04042e')
            lfch_c.pack()
            Label(lfch_c,text="CART ITEM",font=('bold',25),fg='#67e9f0',bg='#04042e').pack()
            lib2=Listbox(lfch_c)
            lib2.pack()
        
            
            query1="SELECT item_id FROM cart WHERE cus_id=%s and cus_id=%s"
            self.cursor.execute(query1,(cus_id,cus_id))
            lst=self.cursor.fetchall()

            query2="SELECT item_id,item_name,price FROM product WHERE item_id=%s and item_id=%s"
            for i in lst:
                self.cursor.execute(query2,(i[0],i[0]))
                l=self.cursor.fetchone()
            
                a,name,price=l
               
                lib2.insert(END,'>{} - Rs.{} - {}'.format(name,price,a))


            def select(lib2,lfch_c):
                lfch_c.destroy()
                lfch_cs=Frame(self.root,height=80,width=160,bg='#04042e')
                lfch_cs.pack()
                lii1=lib2
                lii=lii1.split('-')
                i_id=lii[2].strip()
                query="SELECT item_name,specification,quantity FROM product WHERE item_id=%s and item_id=%s"
                self.cursor.execute(query,(i_id,i_id))
                lst2=self.cursor.fetchone()
                a,b,quantity=lst2
                Label(lfch_cs,text="Product name:{}".format(a),font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
                Label(lfch_cs,text="Specification:{}".format(b),font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
                def buy():
                    lfch_cs.destroy()
                    lfch_csb=Frame(self.root,height=80,width=160,bg='#04042e')
                    lfch_csb.pack()
                    Label(lfch_csb,text="Available quantity::{}".format(quantity),font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=0,column=0)
                    self.customer_buy(i_id,cus_id,address,lfch_csb)

                
                    
                
                
                b2=Button(lfch_cs,text='Confirm',command=buy,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
                b2.pack()
                
                

            def remove(lib2,liib2):
                lii1=liib2
                lii=lii1.split('-')
                i_id=lii[2].strip()
                lib2.delete(ANCHOR)
                self.customer_remove_from_cart(i_id,cus_id,address,lfch_c)
            def back():
                self.customer_home(cus_id,address,lfch_c)


            Button(lfch_c,text='Buy',command=lambda:select(lib2.get(ANCHOR),lfch_c),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            Button(lfch_c,text='Remove from cart',command=lambda:remove(lib2,lib2.get(ANCHOR)),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            Button(lfch_c,text='Back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()

            
        def buyed_product():
            lfch.destroy()
            lfch_bp=Frame(self.root,height=80,width=160,bg='#04042e')
            lfch_bp.pack()
            Label(lfch_bp,text="BUYED PRODUCT",font=('bold',25),fg='#67e9f0',bg='#04042e').pack()
            def back():
                self.customer_home(cus_id,address,lfch_bp)
            Button(lfch_bp,text='back',command=back,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
            lib3=Listbox(lfch_bp,width=50)
            lib3.pack()
            query1="SELECT item_id,quantity,status FROM buyed_product WHERE cus_id=%s and cus_id=%s"
            self.cursor.execute(query1,(cus_id,cus_id))
            lst1=self.cursor.fetchall()

            for i in lst1:
                item_id,quantity,status=i
                self.customer_status(cus_id,item_id)
                query2="SELECT item_name,price,specification FROM product WHERE item_id=%s and item_id=%s"
                self.cursor.execute(query2,(item_id,item_id))
                lst2=self.cursor.fetchone()
                item_name,price,specification=lst2
                lib3.insert(END,">{} - Rs.{} - ({})".format(item_name,price*quantity,status))
            
            
        def logout():
            self.customer_signin(lfch)
        
        
        Label(lfch,text='HOME PAGE',font=('bold',25),fg='#67e9f0',bg='#04042e').pack()
 
        Button(lfch,text='Search item',command=search_item,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(lfch,text='display item',command=display_item,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(lfch,text='Cart',command=cart,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(lfch,text='Buyed product',command=buyed_product,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        Button(lfch,text='Logout',command=logout,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()







    def customer_remove_from_cart(self,item_id,cus_id,address,lfch_c):
        query="DELETE FROM cart WHERE item_id=%s and cus_id=%s"
        self.cursor.execute(query,(item_id,cus_id))
        self.cnx.commit()
        Label(lfch_c,text="Item removed from the cart",font=('bold',15),fg='#67e9f0',bg='#04042e').pack()
       # self.customer_home(cus_id,address,lfch_c)



    def customer_status(self,cus_id,item_id):
        query1="SELECT ordered_date,delivery_date FROM buyed_product WHERE cus_id=%s and item_id=%s"
        self.cursor.execute(query1,(cus_id,item_id))
        lst1=self.cursor.fetchone()
        ordered_date,delivery_date=lst1
        today=date.today()+timedelta(7)
        if(today==ordered_date):
            query1="UPDATE buyed_product SET status='Not delivered' WHERE cus_id=%s and item_id=%s"
            self.cursor.execute(query1,(cus_id,item_id))
            self.cnx.commit()
        elif(today==delivery_date):
            query2="UPDATE buyed_product SET status='Delivered' WHERE cus_id=%s and item_id=%s"
            self.cursor.execute(query2,(cus_id,item_id))
            self.cnx.commit()
        elif(today>delivery_date):
            query3="UPDATE buyed_product SET status='Delivered' WHERE cus_id=%s and item_id=%s"
            self.cursor.execute(query3,(cus_id,item_id))
            self.cnx.commit()
        




    def customer_buy(self,item_id,cus_id,address,prev):
        def buy(quant):
            prev.destroy()
            prev1=Frame(self.root,height=80,width=160,bg='#04042e')
            prev1.pack()
            delivery_date=date.today()+timedelta(7)
            ordered_date=date.today()
            quantity=int(quant)
            query1="INSERT INTO buyed_product(cus_id,item_id,quantity,address,ordered_date,delivery_date) VALUES(%s,%s,%s,%s,%s,%s)"
            self.cursor.execute(query1,(cus_id,item_id,quantity,address,ordered_date,delivery_date))
            self.cnx.commit()

            query2="UPDATE product SET quantity=quantity-%s WHERE item_id=%s"
            self.cursor.execute(query2,(quantity,item_id))
            self.cnx.commit()

            query4="UPDATE buyed_product SET status='Not delivered' WHERE item_id=%s and cus_id=%s"
            self.cursor.execute(query4,(item_id,cus_id))
            self.cnx.commit()

            query3="SELECT item_name,price FROM product WHERE item_id=%s and item_id=%s"
            self.cursor.execute(query3,(item_id,item_id))
            lst=self.cursor.fetchone()
            item_name,price=lst

            lb1=Label(prev1,text="item name:{}".format(item_name),font=('bold',18),fg='#67e9f0',bg='#04042e')
            lb1.pack()
            lb2=Label(prev1,text="total price:{}".format(quantity*price),font=('bold',18),fg='#67e9f0',bg='#04042e')
            lb2.pack()
            lb3=Label(prev1,text="Delivery date:{}".format(delivery_date),font=('bold',18),fg='#67e9f0',bg='#04042e')
            lb3.pack()
            def backtohome1():
                self.customer_home(cus_id,address,prev1)
            Button(prev1,text="Back to Home",command=backtohome1,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
        
        Label(prev,text="Enter the quantity you want::",font=('bold',18),fg='#67e9f0',bg='#04042e').grid(row=1,column=0)
        quantity=Entry(prev,bg='#02021c',fg='#67e9f0')
        quantity.grid(row=1,column=1)
        b9=Button(prev,text='Submit',command=lambda:buy(quantity.get()),bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10))
        b9.grid()
        
        #prev=Frame(self.root,height=80,width=160,bg='#04042e')
        #rev.grid()
        
        

        
        

    def customer_add_to_cart(self,item_id,cus_id,address,cur_fr):
        query="INSERT INTO cart(cus_id,item_id) VALUES(%s,%s)"
        self.cursor.execute(query,(cus_id,item_id))
        self.cnx.commit()
        
        Label(cur_fr,text="item added to the cart....",font=('bold',18),fg='#67e9f0',bg='#04042e').pack()
        def backtohome():
            self.customer_home(cus_id,address,cur_fr)
        Button(cur_fr,text='Bact to Home',command=backtohome,bg='#080870',fg='#67e9f0',height=2,width=16,font=('bold',10)).pack()
