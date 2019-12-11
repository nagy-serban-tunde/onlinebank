import mysql

class TablesCreated(object):
    def __init__(self, database_name, host, user, password):
        try:
            self.mydb = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    database = database_name
                )
            self.mycursor = self.mydb.cursor()
            print("Successfull connection!")
        except:
            print("Unable connection!")

    def Create_Table_User(self):
        try:
            create_table = "CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) NOT NULL UNIQUE , last_name VARCHAR(255) NOT NULL, first_name VARCHAR(255) NOT NULL , birth_date DATE NOT NULL, profile_picture VARCHAR(255) NOT NULL, created_at DATE NOT NULL, gender ENUM('M','F') NOT NULL, password VARCHAR(255) NOT NULL, email_addres VARCHAR(255)  NOT NULL UNIQUE, phone_number VARCHAR(255) NOT NULL UNIQUE )"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")

    def Create_Table_Deposit(self):
        try:
            create_table = "CREATE TABLE deposit (id INT AUTO_INCREMENT PRIMARY KEY , user_id INT , eur DECIMAL(10,3) DEFAULT 0, ron DECIMAL(10,3) DEFAULT 0, gbp DECIMAL(10,3) DEFAULT 0, usd DECIMAL(10,3) DEFAULT 0, FOREIGN KEY (user_id) REFERENCES user(id))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")
    
    def Create_Table_Transactions(self):
        try:
            create_table = "CREATE TABLE transactions (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, date DATE, FOREIGN KEY (user_id) REFERENCES user(id), type VARCHAR(255))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")
    
    def Create_Table_Income(self):
        try:
            create_table = "CREATE TABLE income (id INT AUTO_INCREMENT PRIMARY KEY, transaction_id INT, amount DECIMAL(10,3), type INT, comment VARCHAR(255) DEFAULT '', FOREIGN KEY (transaction_id) REFERENCES transactions(id))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")
    
    def Create_Table_Types(self):
        try:
            create_table = "CREATE TABLE types_ (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), icon VARCHAR(255) )"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")

    def Create_Table_Expense(self):
        try:
            create_table = "CREATE TABLE expense (id INT AUTO_INCREMENT PRIMARY KEY, transaction_id INT, amount DECIMAL(10,3), type INT, comment VARCHAR(255) DEFAULT '', FOREIGN KEY (transaction_id) REFERENCES transactions(id),FOREIGN KEY (type) REFERENCES types_(id))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")  
        
    def Create_Table_Exchange(self):
        try:
            create_table = "CREATE TABLE exchange (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT, date DATE, FOREIGN KEY (user_id) REFERENCES user(id))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")

    def Create_Table_Exchange_Detail(self):
        try:
            create_table = "CREATE TABLE exchange_detail (id INT AUTO_INCREMENT PRIMARY KEY, exchange_id INT, currency VARCHAR(255), sign VARCHAR(255), from_amount DECIMAL(10,3), to_amount DECIMAL(10,3), rate DECIMAL(10,3), site VARCHAR(255), FOREIGN KEY (exchange_id) REFERENCES exchange(id))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")
    
    def Create_Table_EUR(self):
        try:
            create_table = "CREATE TABLE eur (id INT AUTO_INCREMENT PRIMARY KEY, web_address VARCHAR(255), currency VARCHAR(255), purchase_price DECIMAL(19,3))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")

    def Create_Table_GBP(self):
        try:
            create_table = "CREATE TABLE gbp (id INT AUTO_INCREMENT PRIMARY KEY, web_address VARCHAR(255), currency VARCHAR(255), purchase_price DECIMAL(19,3))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")
    
    def Create_Table_RON(self):
        try:
            create_table = "CREATE TABLE ron (id INT AUTO_INCREMENT PRIMARY KEY, web_address VARCHAR(255), currency VARCHAR(255), purchase_price DECIMAL(19,3))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")
        
    def Create_Table_USD(self):
        try:
            create_table = "CREATE TABLE usd (id INT AUTO_INCREMENT PRIMARY KEY, web_address VARCHAR(255), currency VARCHAR(255), purchase_price DECIMAL(19,3))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")

    def Create_Table_Valuta(self):
        try:
            create_table = "CREATE TABLE Valuta (id INT AUTO_INCREMENT PRIMARY KEY, web_address VARCHAR(255), currency VARCHAR(255), purchase_price DECIMAL(19,3))"
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")

    def main(self):
        self.Create_Table_User()
        self.Create_Table_Deposit()
        self.Create_Table_Transactions()
        self.Create_Table_Income()
        self.Create_Table_Types()
        self.Create_Table_Expense()
        self.Create_Table_Exchange()
        self.Create_Table_Exchange_Detail()
        self.Create_Table_EUR()
        self.Create_Table_GBP()
        self.Create_Table_RON()
        self.Create_Table_USD()
        self.Create_Table_Valuta()
        self.mydb.close()