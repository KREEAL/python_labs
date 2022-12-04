import sqlite3
from xml.dom.minidom import Document
from xml.dom.minidom import *

def make_xml():
    connection = sqlite3.connect("D:\pythonProject\Kharchenko\Database\programms.db")
    cursor = connection.cursor()
    devs = cursor.execute("SELECT * FROM Developer")
    doc = Document()
    catalog = doc.createElement('developers')

    for dev_val in devs:
        dev = doc.createElement('dev')
        id = doc.createElement('id')
        name = doc.createElement('name')
        country = doc.createElement('brand')
        workers_count = doc.createElement('workers_count')

        id.appendChild(doc.createTextNode(str(dev_val[0])))
        name.appendChild(doc.createTextNode(str(dev_val[1])))
        country.appendChild(doc.createTextNode(str(dev_val[2])))
        workers_count.appendChild(doc.createTextNode(str(dev_val[3])))

        dev.appendChild(id)
        dev.appendChild(name)
        dev.appendChild(country)
        dev.appendChild(workers_count)
        catalog.appendChild(dev)

    doc.appendChild(catalog)
    with open("textovik.xml",'w') as f:
        doc.writexml(f,encoding = 'utf-8')
    return doc


# connection = sqlite3.connect("programms.db")
d = make_xml()

# cursor = connection.cursor()
# rows = cursor.execute(f"Insert INTO Os (name,bit) VALUES('{text1}','{text2}')")
# cursor.close()
# connection.commit()
# connection.close()