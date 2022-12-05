
#import xml
#Найти суммарную длину дорог каждого из типов на заданном участке карты
from math import *
import time
import xml.etree.ElementTree as ET


#ФОРМУЛА ГАВЕРСИНУСОВ
def pair_distance(point1,point2):
    fi1 = point1[0]
    fi2 = point2[0]
    deltalambda = abs(point1[0]-point2[0])
    deltanu = 2*asin(  sqrt( sin( (fi2-fi1)/2 )**2 +  cos(fi1)*cos(fi2)*sin( deltalambda/2 )**2 )  )
    #умножаем на радиус земли в метрах. Соответственно, и результат получаем в метрах
    return deltanu*6372795

#Не работает при малых значениях
# def pair_distance(point1,point2):
#     deltanu = math.acos(math.sin(float(point1[0]))*math.sin(float(point2[0]))+math.cos(float(point1[1]))*math.cos(float(point2[1])))
#     return deltanu*6372795

#Теорема пифагора тут точно не сработает
# def pair_distance(point1,point2):
#     return math.sqrt(abs(point1[0]-point2[0])**2+abs(point1[1]-point2[1])**2)

#все элементы под тэгом node
def get_all_nodes(root):
    nodes={}
    for child_node_tag in root.findall('node'):
        id = child_node_tag.attrib['id']
        nodes[id]=(float(child_node_tag.attrib['lat']),float(child_node_tag.attrib['lon']))
    return nodes

#все элементы под тэгом way, содержащие в себе аттрибут, имеющий ключ highway
def get_all_ways_highways(root):
    higways=[]
    for child_way_tag in root.findall('way'):#все линии, но не все из них дороги
        for tag in child_way_tag.findall('tag'):
            if tag.attrib['k']=="highway":
                higways.append(child_way_tag)
    return higways

#Получение всех node, указанные по тегу ref в элементе way
def get_highway_refnodes(way):
    refnodes = []
    for waynode in way.findall('nd'):
        if 'ref' in waynode.attrib:
            refnodes.append(waynode.attrib['ref'])
    return refnodes

#Определяем расстояние, проходя по всем ref node для конкретного way
def get_way_distance(refnodes,all_nodes):
    distance = 0
    for i in range (0,len(refnodes)-1):
        distance+=pair_distance(all_nodes[refnodes[i]],all_nodes[refnodes[i+1]])
    return float(distance)

#получение аттрибута, указывающего на тип дороги (highway)
def get_road_type(way):
    for tag in way.findall('tag'):
        if tag.attrib['k'] == "highway":
            return tag.attrib['v']

def main():
    distances_by_highway_types = {}

    tree1 = ET.parse('15.osm')
    root1 = tree1.getroot()
    tree2 = ET.parse('15_2.osm')
    root2 = tree2.getroot()


    ## Для файла 15.osm

    all_nodes = get_all_nodes(root1)
    all_ways_highways = get_all_ways_highways(root1)


    for way in all_ways_highways:
        current_refnodes = get_highway_refnodes(way)
        way_distance = get_way_distance(current_refnodes,all_nodes)
        road_type = get_road_type(way)
        if road_type not in distances_by_highway_types.keys():
            distances_by_highway_types[road_type]=float(way_distance)
        else:
            distances_by_highway_types[road_type] =float(distances_by_highway_types[road_type])+float(way_distance)

    print('АНАПА!  ',distances_by_highway_types)
    distances_by_highway_types_root1=distances_by_highway_types

    #Для файла 15_2


    distances_by_highway_types={}

    all_nodes = get_all_nodes(root2)
    all_ways_highways = get_all_ways_highways(root2)

    for way in all_ways_highways:
        current_refnodes = get_highway_refnodes(way)
        way_distance = get_way_distance(current_refnodes, all_nodes)
        road_type = get_road_type(way)
        if road_type not in distances_by_highway_types.keys():
            distances_by_highway_types[road_type] = float(way_distance)
        else:
            distances_by_highway_types[road_type] = float(distances_by_highway_types[road_type]) + float(way_distance)

    print("КАЗАНЬ!  ",distances_by_highway_types)
    distances_by_highway_types_root2 = distances_by_highway_types



if __name__ == "__main__":
    main()
