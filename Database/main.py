import sqlite3
from xml.dom.minidom import *

connection = sqlite3.connect("programms.db")
cursor = connection.cursor()
rows = cursor.execute("Select * FROM OS").fetchall()
print(rows)

print(connection.total_changes)