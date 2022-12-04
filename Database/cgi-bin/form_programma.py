#!/usr/bin/env python3
import cgi
import sqlite3

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")
text3 = form.getfirst("TEXT_3", "не задано")
text4 = form.getfirst("TEXT_4", "не задано")

connection = sqlite3.connect("programms.db")
cursor = connection.cursor()
rows = cursor.execute(f"Insert INTO Program (developer,os,name,version) VALUES('{text1}','{text2}','{text3}','{text4}')")
cursor.close()
connection.commit()
connection.close()


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>Name: {}</p>".format(text1))
print("<p>Razrabotchick: {}</p>".format(text2))
print("<p>OS: {}</p>".format(text3))
print("<p>Version: {}</p>".format(text4))

print("""</body>
        </html>""")