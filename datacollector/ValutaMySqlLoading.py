import mysql.connector
import json

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
       
    def Read_Json_File_and_Update_Database(self,json_file):
        with open(json_file,'r') as myfile:
            data = myfile.read()
        json_data = json.loads(data)
        is_empty_tables = "SELECT count(*) from {0}".format(self.table_name)
        is_empty = self.mycursor.execute(is_empty_tables)
        is_empty = self.mycursor.fetchall()
        is_empty,= is_empty[0]
        id_elem = 0
        for element in json_data:
            if is_empty == 0:
                try:
                    insert_element = "INSERT INTO {0} (web_address, currency, purchase_price) VALUES (%s, %s, %s)".format(self.table_name)
                    val = (element['web_address'],element['currency'],element['purchase_price'])
                    self.mycursor.execute(insert_element, val)
                    self.mydb.commit()
                    print("Data inserted successfull in", self.table_name)
                except:
                    print("Unable to inserte the data!", self.table_name)
            else:
                try:
                    id_str = str(id_elem+1)
                    update_table = "UPDATE {0} SET web_address = %s, currency = %s, purchase_price = %s WHERE id = %s".format(self.table_name)
                    val = (element['web_address'],element['currency'],element['purchase_price'],id_str)
                    self.mycursor.execute(update_table,val)
                    self.mydb.commit()
                    id_elem += 1 
                    print("Data updated successfull in", self.table_name)
                except:
                    print("Unable to update the data in", self.table_name)
        self.mydb.close()
        
        