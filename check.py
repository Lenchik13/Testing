import mysql.connector
from model.contact import Contact

connection = mysql.connector.connect(host="127.0.0.1", database="addressbook", user="root", password = "")

list = []
cursor = connection.cursor()
try:
    cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
    for row in cursor:
        (id, firstname, lastname) = row
        list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
finally:
    cursor.close()
print(list)