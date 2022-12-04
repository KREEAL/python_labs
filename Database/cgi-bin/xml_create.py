#!/usr/bin/env python3
import cgi
import sqlite3
from xml.dom.minidom import *


form = cgi.FieldStorage()

connection = sqlite3.connect("programms.db")
cursor = connection.cursor()
cursor.execute(f"Select * from Developer")
devs = cursor.fetchall()
cursor.close()
connection.close()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Просмотр содержимого базы</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
        </head>
        <body>""")

print("<h1>ОС</h1>")
for row in devs:
    print("<h3>{}</h3>".format(row))


print("""</body>
        </html>""")