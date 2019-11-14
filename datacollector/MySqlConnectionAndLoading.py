import mysql.connector

mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="diak123",
        database = "seged"
    )

ls = [['https://www.otpbank.ro/hu/valutarfolyam', 'GBP', 'RON', '5.428', '5.672'], ['http://www.lillapanzio.ro/valutavalto', 'GBP', 'EUR', '1.152', '1.157'], ['http://www.lillapanzio.ro/valutavalto', 'GBP', 'USD', '1.277', '1.277']]

mycursor = mydb.cursor()

sql = "DROP TABLE BestChangeValutaRON"

mycursor.execute(sql)

mycursor.execute("CREATE TABLE BestChangeValutaRON (web_address VARCHAR(255), chan VARCHAR(255), currency VARCHAR(255), purchase_price VARCHAR(255), sale_price VARCHAR(255))")

sql = "INSERT INTO BestChangeValutaRON (web_address, chan, currency, purchase_price, sale_price) VALUES (%s, %s, %s, %s, %s)"
val = ("John", "Highway 21","Highway 21","Highway 21","Highway 21")

mycursor.execute(sql, val)

mydb.commit()