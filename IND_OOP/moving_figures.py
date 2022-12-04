from Pentagon import Pentagon
from Quad import Quad

p = Pentagon('1',0,0,40)
print(p.get_coordinates())
p.move(2,0)
print(p.get_coordinates())

q = Quad('1',1,0,0)
print(q.get_coordinates())

#print(q.intersect_otrezkov((0,0),(2,0),(1,1),(1,10)))
print(p.is_intersect(q))