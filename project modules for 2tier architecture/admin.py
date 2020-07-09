from datetime import date,timedelta
class Admin:
    def __init__(self,cursor,cnx):
        self.cursor=cursor
        self.cnx=cnx

    def admin_signin(self):
        print("------------------------------")
        print("         SIGNIN PAGE          ")
        print("------------------------------")
        name=input("Enter your name:")
        password=input("Enter your password:")
        query="SELECT name,password FROM admin WHERE name=%s and password=%s"
        self.cursor.execute(query,(name,password))
        val=self.cursor.fetchone()

    
        if(val==None):
            print("Wrong password")
        else:
            self.admin_home()

    
    def admin_product(self):
        query="SELECT item_id,item_name,quantity,price FROM product"
        self.cursor.execute(query)
        lst=self.cursor.fetchall()   
        for item in lst:
            a,b,c,d=item
            print('+{} - {} - {} - Rs{}'.format(a,b,c,d))
        c=int(input('''
            1.add product
            2.remove product
            3.back
            '''))
        if(c==1):
           item_id=input("Enter the item ID:") 
           item_name=input("Enter the item name:")
           price=int(input("Enter price of the item:"))
           specification=input("Enter item specificaiton:")
           quantity=int(input("Enter the quantity:"))
           query="INSERT INTO product(item_id,item_name,price,specification,quantity) VALUES(%s,%s,%s,%s,%s)"
           self.cursor.execute(query,(item_id,item_name,price,specification,quantity))
           self.cnx.commit()
           print("added succesfully")
           self.admin_home()
        elif(c==2):
            item_id=input("Enter the item ID")
            query="DELETE FROM product WHERE item_id=%s and item_id=%s"
            self.cursor.execute(query,(item_id,item_id))
            self.cnx.commit()
            print("Removed successfully")
            self.admin_home()
        elif(c==3):
            self.admin_home()
        else:
            print("Invalid entry")

    def admin_quantity(self):
        print('''
            1.add quantity
            2.remove quantity
            3.back
            ''')
        ch=int(input("Enter your choice:"))
        if(ch==1):
            query="SELECT item_id,item_name,quantity FROM product"
            self.cursor.execute(query)
            lst=self.cursor.fetchall()   
            for item in lst:
                a,b,c=item
                print('>{} - {} - {}'.format(a,b,c))

            item_id=input("Enter the item ID:")
            q="SELECT item_name FROM product WHERE item_id=%s and item_id=%s"
            self.cursor.execute(q,(item_id,item_id))
            i=self.cursor.fetchone()
            prod_name=i[0]
            choice=input('sure this ({}) product [yes/no]? '.format(prod_name))
            if(choice=='yes' or choice=='y'):
                aq=input("Enter the number of quantity:")
                query="UPDATE product SET quantity=quantity+%s WHERE item_id=%s"
                self.cursor.execute(query,(aq,item_id))
                self.cnx.commit()
                print(aq+" item added successfully")
                self.admin_home()
            elif(choice=='no' or choice=='n'):
                self.admin_quantity()

        elif(ch==2):
            query="SELECT item_id,item_name,quantity FROM product"
            self.cursor.execute(query)
            lst=self.cursor.fetchall()   
            for item in lst:
                a,b,c=item
                print('+{} - {} - {}'.format(a,b,c))
            item_id=input("Enter the item ID:")
            q="SELECT item_name FROM product WHERE item_id=%s and item_id=%s"
            self.cursor.execute(q,(item_id,item_id))
            i=self.cursor.fetchone()
            prod_name=i[0]
            choice=input('sure this ({}) product [yes/no]? '.format(prod_name))
            if(choice=='yes' or choice=='y'):
                rq=input("Enter the number of quantity:")
                query="UPDATE product SET quantity=quantity-%s WHERE item_id=%s"
                self.cursor.execute(query,(rq,item_id))
                self.cnx.commit()
                print(rq+" item removed successfully")
                self.admin_home()
            elif(choice=='no' or choice=='n'):
                self.admin_quantity()
        elif(ch==3):
            self.admin_home()
        else:
            print("Invalid entry")
            self.admin_home()


    def admin_view_product(self):
        query="SELECT item_id,item_name,quantity FROM product"
        self.cursor.execute(query)
        lst=self.cursor.fetchall()   
        for item in lst:
            a,b,c=item
            print('>{} - {} - {}'.format(a,b,c))
        self.admin_home()

    def admin_view_customer(self):
        query1="SELECT cus_id,name FROM customer"
        self.cursor.execute(query1)
        lst1=self.cursor.fetchall()
        for i in lst1:
            id,name=i
            print(">{} - {}".format(id,name))
        cus_id=input("Enter the customerID:")
        query2="SELECT name,phone_no,address FROM customer WHERE cus_id=%s and cus_id=%s"
        self.cursor.execute(query2,(cus_id,cus_id))
        lst2=self.cursor.fetchone()
        name,phone_no,address=lst2
        print("Name:",name)
        print("Phone Number:",phone_no)
        print("Address:",address)
        query3="SELECT item_id,quantity,delivery_date FROM buyed_product WHERE cus_id=%s and cus_id=%s"
        self.cursor.execute(query3,(cus_id,cus_id))
        lst3=self.cursor.fetchall()
        for i in lst3:
            item_id,quantity,delivery_date=i
            query4='SELECT item_name,price FROM product WHERE item_id=%s and item_id=%s'
            self.cursor.execute(query4,(item_id,item_id))
            lst4=self.cursor.fetchone()
            item_name,price=lst4
            print('Item Name:',item_name)
            print("quantity:",quantity)
            print("Total price:",quantity*price)
        



        self.admin_home()
        
        
    def admin_home(self):
        
        print("------------------------------")
        print("            ADMIN             ")
        print("------------------------------")
        print('''
         1.make changes in product
         2.make changes in quantity
         3.view the product
         4.view the customer
         5.logout

        ''' )
        choice=int(input("Enter your choice:"))
        if(choice==1):
            self.admin_product()
            self.admin_home()
        elif(choice==2):
            self.admin_quantity()
            self.admin_home()
        elif(choice==3):
            self.admin_view_product()
            self.admin_home()
        elif(choice==4):
            self.admin_view_customer()
            self.admin_home()
        elif(choice==5):
            pass
        else:
            print("Invalid entry")
