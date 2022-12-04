from xml.dom import minidom
from xml.dom.minidom import *
import sqlite3

def InsertFromXML(xml):
    """
    Выводим все заголовки из xml.
    """
    db = sqlite3.connect("D:\pythonProject\Kharchenko\Database\programms.db")
    cursor = db.cursor()

    doc = minidom.parse(xml)
    node = doc.documentElement
    buses = doc.getElementsByTagName("dev")

    names = []
    brends = []
    workers_counts = []
    for bus in buses:
        name = bus.getElementsByTagName("name")[0]
        brend = bus.getElementsByTagName("brand")[0]
        workers_count = bus.getElementsByTagName("workers_count")[0]
        names.append(name)
        brends.append(brend)
        workers_counts.append(workers_count)

    for i in range(len(names)):
        nodes = names[i].childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                names[i] = node.data

    for i in range(len(brends)):
        nodes = brends[i].childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                brends[i] = node.data

    for i in range(len(workers_counts)):
        nodes = workers_counts[i].childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                workers_counts[i] = node.data

    for i in range(len(names)):
        cursor.execute(f"Insert INTO Developer (name,country,workers_count) VALUES('{str(names[i])}','{str(brends[i])}','{str(workers_counts[i])}')")
        db.commit()

InsertFromXML("textovik_insert.xml")