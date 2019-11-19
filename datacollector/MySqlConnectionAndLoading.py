import mysql.connector

class MySqlConnectionAndLoading(object):
    def __init__(self, ListToData, table_name,database_name,host,user,password):
        self.ListToData = ListToData
        self.table_name = table_name
        self.mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database = database_name
            )
        self.mycursor = self.mydb.cursor()

    def Drop_Table(self):
        try:
            drop_table = "DROP TABLE {0}".format(self.table_name)
            self.mycursor.execute(drop_table)
            print("Table droped successfull!")
        except:
            print("Unable to drop the table!")

    def Create_Table(self):
        try:
            create_table = "CREATE TABLE {0} (id INT NOT NULL AUTO_INCREMENT, web_address VARCHAR(255), currency VARCHAR(255), purchase_price DECIMAL(19,3),PRIMARY KEY (id))".format(self.table_name)
            self.mycursor.execute(create_table)
            print("Table created successfull!")
        except:
            print("Unable to create the table")
    
    def Insert_Element_In_Table(self):
        try:
            for element in self.ListToData:
                insert_element = "INSERT INTO {0} (web_address, currency, purchase_price) VALUES (%s, %s, %s)".format(self.table_name)
                val = (element[0],element[2],element[3])
                self.mycursor.execute(insert_element, val)
                self.mydb.commit()
                print("Data inserted successfull!")
        except:
            print("Unable to inserte the data!")
    
    def Update_Element_In_Table(self):
        try:
            for id_elem in range(len(self.ListToData)):
                id_str = str(id_elem+1)
                update_table = "UPDATE {0} SET web_address = %s, currency = %s, purchase_price = %s WHERE id = %s".format(self.table_name)
                val = (self.ListToData[id_elem][0],self.ListToData[id_elem][2],self.ListToData[id_elem][3],id_str)
                self.mycursor.execute(update_table,val)
                self.mydb.commit()
                print("Data updated successfull!")
        except:
            print("Unable to update the data!")

    def main(self):
        self.Drop_Table()
        self.Create_Table()
        self.Insert_Element_In_Table()
        # self.Update_Element_In_Table()
        self.mydb.close()
        