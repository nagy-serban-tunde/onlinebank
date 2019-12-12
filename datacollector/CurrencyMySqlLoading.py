import mysql.connector

"""This script loads data to the database"""

class CurrencyMySqlLoading(object):
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
    
    def Insert_Or_Update_Element_In_Table(self):
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
                    print("Data inserted successfull in ",self.table_name)
            except:
                print("Unable to inserte the data in ",self.table_name)
        else:
            try:
                for id_elem in range(len(self.ListToData)):
                    id_str = str(id_elem+1)
                    update_table = "UPDATE {0} SET web_address = %s, currency = %s, purchase_price = %s WHERE id = %s".format(self.table_name)
                    val = (self.ListToData[id_elem][0],self.ListToData[id_elem][2],self.ListToData[id_elem][3],id_str)
                    self.mycursor.execute(update_table,val)
                    self.mydb.commit()
                    print("Data updated successfull in", self.table_name)
            except:
                print("Unable to update the data in", self.table_name)
        self.mydb.close()

    def CurrencyTableUpload(self, webpages_name):
        webpageindex = 0
        for index in range(len(self.ListToData)):
            if index == 3 or index == 6:
                webpageindex += 1
            self.ListToData[index] = [webpages_name[webpageindex]] + self.ListToData[index]
        self.Insert_Or_Update_Element_In_Table()
        