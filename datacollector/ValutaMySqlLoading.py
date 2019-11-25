import mysql.connector

class ValutaMySqlLoading(object):
    def __init__(self, ListToData, table_name,database_name,host,user,password):
        self.ListToData = ListToData
        self.table_name = table_name
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
    
    def Insert_Element_In_Table(self):
        is_empty_tables = "SELECT count(*) from {0}".format(self.table_name)
        is_empty = self.mycursor.execute(is_empty_tables)
        is_empty = self.mycursor.fetchall()
        is_empty,= is_empty[0]
        if is_empty == 0:
            try:
                for element in self.ListToData:
                    insert_element = "INSERT INTO {0} (web_address, currency, purchase_price) VALUES (%s, %s, %s)".format(self.table_name)
                    val = (element[0],element[2],element[3])
                    self.mycursor.execute(insert_element, val)
                    self.mydb.commit()
                    print("Data inserted successfull!")
            except:
                print("Unable to inserte the data!")
        else:
            pass
    
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
        # self.Drop_Table()
<<<<<<< HEAD
        # self.Insert_Element_In_Table()
=======
>>>>>>> b4a84a49c924f0729d84b831eb7066a77ff68ad8
        self.Update_Element_In_Table()
        self.Insert_Element_In_Table()
        self.mydb.close()
        