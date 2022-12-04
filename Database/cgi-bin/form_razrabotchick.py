#!/usr/bin/env python3
import cgi
import sqlite3

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")
text3 = form.getfirst("TEXT_3", "не задано")

connection = sqlite3.connect("programms.db")
cursor = connection.cursor()
rows = cursor.execute(f"Insert INTO Developer (name,country,workers_count) VALUES('{text1}','{text2}','{text3}')")
cursor.close()
connection.commit()
connection.close()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>Name: {}</p>".format(text1))
print("<p>Country: {}</p>".format(text2))
print("<p>Workers count: {}</p>".format(text3))

print("""</body>
        </html>""")