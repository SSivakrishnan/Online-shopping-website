from customer import *
from admin import *
import mysql.connector
from datetime import date,timedelta
cnx=mysql.connector.connect(user="root",database="online_shopping")
cursor=cnx.cursor(buffered=True)
while True:
    print("================================")
    who=input("  Admin or Customer:")
    print("================================")

    if(who=="admin" or who=="a"):
        ad=Admin(cursor,cnx)
        ad.admin_signin()
         
    elif(who=="customer" or who=="c"):
        cus=Customer(cursor,cnx)
        sign=input("'signin' or 'sigup':")
        if(sign=="signin"):
            cus.customer_signin()
        elif(sign=='signup'):
            cus.customer_signup()
        else:
            print("Invalid data")
    else:
        print("Invalid data")
        