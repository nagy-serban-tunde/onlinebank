import mysql

class TablesCreated(object):
    def __init__(self, database_name, host, user, password):
        self.mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database = database_name
            )
        self.mycursor = self.mydb.cursor()

    def Create_Table_User(self):
        try:
            create_table = "CREATE TABLE user (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, full_name VARCHAR(255), birth_date TIMESTAMP, profile_picture VARCHAR(255), created_at TIMESTAMP, gender VARCHAR(255), password VARCHAR(255), email_addres VARCHAR(255), phone_number VARCHAR(255), deposit DECIMAL)"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")
    
    def Create_Table_Transactions(self):
        try:
            create_table = "CREATE TABLE transactions (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, user_id INT, date TIMESTAMP, FOREIGN KEY (id) REFERENCES user(id))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")
    
    def Create_Table_Income(self):
        try:
            create_table = "CREATE TABLE income (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, transaction_id INT, amount DECIMAL, FOREIGN KEY (id) REFERENCES transactions(id))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")
    
    def Create_Table_Types(self):
        try:
            create_table = "CREATE TABLE types_ (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), icon VARCHAR(255) )"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")

    def Create_Table_Expense(self):
        try:
            create_table = "CREATE TABLE expense (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, transaction_id INT, amount DECIMAL, type INT, FOREIGN KEY (id) REFERENCES transactions(id),FOREIGN KEY (type) REFERENCES types_(id))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")  
        
    def Create_Table_Exchange(self):
        try:
            create_table = "CREATE TABLE exchange (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, user_id INT, date TIMESTAMP, FOREIGN KEY (id) REFERENCES user(id))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")

    def Create_Table_Exchange_Detail(self):
        try:
            create_table = "CREATE TABLE exchange_detail (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, exchange_id INT, currency VARCHAR(255), sign VARCHAR(255), from_amount DECIMAL, to_amount DECIMAL, rate DECIMAL, site VARCHAR(255), FOREIGN KEY (exchange_id) REFERENCES exchange(id))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")

    def main(self):
        self.Create_Table_User()
        self.Create_Table_Transactions()
        self.Create_Table_Income()
        self.Create_Table_Types()
        self.Create_Table_Expense()
        self.Create_Table_Exchange()
        self.Create_Table_Exchange_Detail()
        self.mydb.close()