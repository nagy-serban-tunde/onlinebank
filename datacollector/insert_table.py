import mysql.connector

def InsertToTable():
    mydb = mysql.connector.connect(
                        host= "127.0.0.1",
                        user= "root",
                        password= "diak123",
                        database = "online_bank"
                    )
    mycursor = mydb.cursor()

    """Table types"""
    insert_element = "INSERT INTO types_ (id,name,icon) VALUES(%s,%s,%s)"
    value = ("1","Public Transport","fas fa-bus")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO types_ (id,name,icon) VALUES(%s,%s,%s)"
    value = ("2","Food","fas fa-utensils")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO types_ (id,name,icon) VALUES(%s,%s,%s)"
    value = ("3","Housing","fas fa-home")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO types_ (id,name,icon) VALUES(%s,%s,%s)"
    value = ("4","Income","fas fa-coins")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO types_ (id,name,icon) VALUES(%s,%s,%s)"
    value = ("5","Shopping","fas fa-shopping-bag")
    mycursor.execute(insert_element,value)
    mydb.commit()

    """Table user"""
    insert_element = "INSERT INTO user (id,username,last_name,first_name,birth_date,profile_picture,created_at,gender,password,email_addres,phone_number) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    value = ("1","nagytunde","Nagy","Tunde","2019.09.05","kep","2019.11.30","F","diak1234","nagyserbantunde@gmail.com","0729461356")
    mycursor.execute(insert_element,value)
    mydb.commit()

    """Table deposit"""
    insert_element = "INSERT INTO deposit (id,user_id,eur,ron,gbp,usd) VALUES(%s,%s,%s,%s,%s,%s)"
    value = ("1","1","20","22","23.5","236.3")
    mycursor.execute(insert_element,value)
    mydb.commit()

    """Transactions"""
    insert_element = "INSERT INTO transactions (id,user_id,date) VALUES(%s,%s,%s)"
    value = ("1","1","2019.11.30")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO transactions (id,user_id,date) VALUES(%s,%s,%s)"
    value = ("2","1","2019.11.10")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO transactions (id,user_id,date) VALUES(%s,%s,%s)"
    value = ("3","1","2019.11.30")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO transactions (id,user_id,date) VALUES(%s,%s,%s)"
    value = ("4","1","2019.11.30")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO transactions (id,user_id,date) VALUES(%s,%s,%s)"
    value = ("5","1","2019.11.30")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO transactions (id,user_id,date) VALUES(%s,%s,%s)"
    value = ("6","1","2019.11.30")
    mycursor.execute(insert_element,value)
    mydb.commit()

    """Table income"""
    insert_element = "INSERT INTO income (id,transaction_id,amount) VALUES(%s,%s,%s)"
    value = ("1","1","1236")
    mycursor.execute(insert_element,value)
    mydb.commit()

    """Table expense"""
    insert_element = "INSERT INTO expense (id,transaction_id,amount,type) VALUES(%s,%s,%s,%s)"
    value = ("1","2","12","1")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO expense (id,transaction_id,amount,type) VALUES(%s,%s,%s,%s)"
    value = ("2","3","24","2")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO expense (id,transaction_id,amount,type) VALUES(%s,%s,%s,%s)"
    value = ("3","4","32","5")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO expense (id,transaction_id,amount,type) VALUES(%s,%s,%s,%s)"
    value = ("4","5","100","4")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO expense (id,transaction_id,amount,type) VALUES(%s,%s,%s,%s)"
    value = ("5","6","200","4")
    mycursor.execute(insert_element,value)
    mydb.commit()

    """Table exchange"""
    insert_element = "INSERT INTO exchange (id,user_id,date) VALUES(%s,%s,%s)"
    value = ("1","1","2019.11.29")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO exchange (id,user_id,date) VALUES(%s,%s,%s)"
    value = ("2","1","2019.11.29")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO exchange (id,user_id,date) VALUES(%s,%s,%s)"
    value = ("3","1","2019.11.29")
    mycursor.execute(insert_element,value)
    mydb.commit()

    """Table exchanged detail"""
    insert_element = "INSERT INTO exchange_detail (id,exchange_id,currency,sign,from_amount,to_amount,rate,site) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    value = ("1","1","RON","EUR","50","10.45","0.20","https://www.otpbank.ro/hu/valutarfolyam")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO exchange_detail (id,exchange_id,currency,sign,from_amount,to_amount,rate,site) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    value = ("2","2","RON","EUR","50","15.68","0.20","https://www.otpbank.ro/hu/valutarfolyam")
    mycursor.execute(insert_element,value)
    mydb.commit()

    insert_element = "INSERT INTO exchange_detail (id,exchange_id,currency,sign,from_amount,to_amount,rate,site) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    value = ("3","3","RON","EUR","100","20.90","0.20","https://www.otpbank.ro/hu/valutarfolyam")
    mycursor.execute(insert_element,value)
    mydb.commit()

    mydb.close()