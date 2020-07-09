from datetime import date,timedelta
class Customer:
    def __init__(self,cursor,cnx):
        self.cursor=cursor
        self.cnx=cnx
    def customer_signup(self):
        print("------------------------------")
        print("          SIGN UP             ")
        print("------------------------------")
        cus_id=input("Enter your id:")
        name=input("Enter your name:")
        phone_no=input("Enter your phone number:")
        password=input("Enter the password")
        address=input("Enter your address:")
        query="INSERT INTO customer(cus_id,name,phone_no,password,address) VALUES( %s, %s, %s,%s,%s)"
        self.cursor.execute(query,(cus_id,name,phone_no,password,address))
        self.cnx.commit()
        self.customer_home( )
    def customer_signin(self):
        print("------------------------------")
        print("           SIGNIN             ")
        print("------------------------------")
        name=input("Enter your name:")
        password=input("Enter your password:")
        query="SELECT name,password FROM customer WHERE name=%s and password=%s"
        self.cursor.execute(query,(name,password))
        val=self.cursor.fetchone()

        query="SELECT cus_id FROM customer WHERE name=%s and password=%s"
        self.cursor.execute(query,(name,password))
        cus=self.cursor.fetchone()
        cus_id=cus[0]

        query="SELECT address FROM customer WHERE name=%s and password=%s"
        self.cursor.execute(query,(name,password))
        addd=self.cursor.fetchone()
        address=addd[0]

        if(val==None):
            print("Wrong password")
        else:
            self.customer_home(cus_id,address)

    def customer_home(self,cus_id,address):

    
        print("------------------------------")
        print("          Home page           ")
        print("------------------------------")
        print('''
            1.Search item
            2.display item
            3.Cart
            4.Buyed product
            5.Logout
        ''')
        choice=int(input("Enter your choice:"))
        if(choice==1):
            item=input("Enter the item:")
            query="SELECT item_id,item_name,price,specification,quantity FROM product WHERE item_name=%s and item_name=%s"
            self.cursor.execute(query,(item,item))
            i=self.cursor.fetchone()
            item_id,item_name,price,specification,quantity=i
            print('{} - {}- Rs.{} - {} '.format(item_id,item_name,price,specification))
            
            print('''
            1.Buy
            2.Add to cart
            3.back
            ''')
            ch=int(input("Enter your choice:"))
            if(ch==1):
                print("Available quantity::",quantity)
                self.buy(item_id,cus_id,address)
            elif(ch==2):
                self.add_to_cart(item_id,cus_id,address)
            elif(ch==3):
                self.customer_home(cus_id,address)
            else:
                print("Invalid entry")
                self.customer_home(cus_id,address)


        elif(choice==2):
            query="SELECT item_id,item_name,price FROM product"
            self.cursor.execute(query)
            lst1=self.cursor.fetchall()   
            print("item ID - item name   -   price ")
            for item in lst1:
                a,b,c=item
                print('>{} - {} - Rs.{}'.format(a,b,c)) 
            i_id=input("Enter the itemID going to buy:")
            query="SELECT item_name,specification,quantity FROM product WHERE item_id=%s and item_id=%s"
            self.cursor.execute(query,(i_id,i_id))
            lst2=self.cursor.fetchone()
            a,b,quantity=lst2
            print("------------------------------------")
            print("Product name:",a)
            print("Specification:",b)
            
            print("------------------------------------")
            print('''
            1.Buy
            2.Add to cart
            3.back
            ''')
            
            ch=int(input("Enter your choice:"))
            if(ch==1):
                print("Available quantity::",quantity)
                self.customer_buy(i_id,cus_id,address)
                self.customer_home(cus_id,address)
            elif(ch==2):
                self.customer_add_to_cart(i_id,cus_id,address)
                self.customer_home(cus_id,address)
            elif(ch==3):
                self.customer_home(cus_id,address)
            else:
                print("Invalid entry")
        elif(choice==3):
            print("------------------------------")
            print("         CART ITEM            ")
            print("------------------------------")
            query1="SELECT item_id FROM cart WHERE cus_id=%s and cus_id=%s"
            self.cursor.execute(query1,(cus_id,cus_id))
            lst=self.cursor.fetchall()
            query2="SELECT item_id,item_name,price FROM product WHERE item_id=%s and item_id=%s"
            for i in lst:
                self.cursor.execute(query2,(i[0],i[0]))
                l=self.cursor.fetchone()
                a,name,price=l
                print('>{} - {} - Rs.{}'.format(a,name,price))
            
            
            print('''
            1.Buy
            2.Remove from the cart
            3.Back
            ''')
            n=int(input("Enter the choice:"))
            if(n==1):
                i_id=input("Enter the itemID going to buy:")
                self.customer_buy(i_id,cus_id,address)
                self.customer_home(cus_id,address)
            elif(n==2):
                i_id=input("Enter the itemID going to remove:")
                self.customer_remove_from_cart(i_id,cus_id,address)
                self.customer_home(cus_id,address)
            elif(n==3):
                self.customer_home(cus_id,address)
            else:
                print("Invalid entry")
                self.customer_home(cus_id,address)


            
        elif(choice==4):
            
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
                print(">{} - Rs.{} - {} - ({})".format(item_name,price*quantity,specification,status))
            self.customer_home(cus_id,address)

        elif(choice==5):
            pass
        else:
            print("Invalid entry")

    def customer_remove_from_cart(self,item_id,cus_id,address):
        query="DELETE FROM cart WHERE item_id=%s and cus_id=%s"
        self.cursor.execute(query,(item_id,cus_id))
        self.cnx.commit()
        print("Item removed from the cart")
        self.customer_home(cus_id,address)



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
        




    def customer_buy(self,item_id,cus_id,address):
        quantity=int(input("Enter the quantity you want::"))
        delivery_date=date.today()+timedelta(7)
        ordered_date=date.today()
        
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
        print("item name:",item_name)
        print("total price:",quantity*price)
        print("Delivery date:",delivery_date)

        

    def customer_add_to_cart(self,item_id,cus_id,address):
        query="INSERT INTO cart(cus_id,item_id) VALUES(%s,%s)"
        self.cursor.execute(query,(cus_id,item_id))
        self.cnx.commit()

        print("item added to the cart....")
        self.customer_home(cus_id,address)
