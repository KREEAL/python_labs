import math
from Quad import Quad

class Pentagon:
    def __init__(self, name, x, y,r):
        self.name = name
        try:
            if r<=0:
                r = 0
                r = r/r
            self.r = r
        except ZeroDivisionError:
            print('Ошибка создания фигуры. Выбрано базовое значение большего радиуса = 5')
        self.center_x = x
        self.center_y = y


    def initiate_coordinates(self):
        self.coords = [(self.center_x + self.r * math.cos(2 * math.pi * i / 5), self.center_y + self.r * math.sin(2 * math.pi * i / 5)) for i in
                  range(1, 5 + 1)]

    def rotate(self,alfa):
        alfa = alfa*math.pi/180
        for i in range(5):
            x = self.coords[i][0]*math.cos(alfa) - self.coords[i][1]*math.sin(alfa)
            y = self.coords[i][0]*math.sin(alfa) + self.coords[i][1]*math.cos(alfa)
            self.coords[i]=(x,y)

    def move(self, x, y):
        self.center_x = self.center_x + x
        self.center_y = self.center_y + y
        self.initiate_coordinates()

    def get_coordinates(self) -> list:
        self.initiate_coordinates()
        return self.coords

    def rotate_tochki(self, a, b, c):
        return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])

    def intersect_otrezkov(self, a, b, c, d):
        return self.rotate_tochki(a, b, c) * self.rotate_tochki(a, b, d) <= 0 and self.rotate_tochki(c, d,
                                                                                                     a) * self.rotate_tochki(
            c, d, b) < 0

    def is_intersect(self, quadra: Quad):
        qube_cords = quadra.get_coordinates()
        penta_pairs = list()
        for i in range(4):
            penta_pairs.append((self.coords[i], self.coords[i + 1]))
        penta_pairs.append((self.coords[4], self.coords[0]))
        print(penta_pairs)
        bigger_penta = Quad('temp', self.r * 1.1, self.center_x, self.center_y)
        bigger_penta.rotate(15)
        bigger_penta_pairs = list()
        for i in range(4):
             bigger_penta_pairs.append((bigger_penta.get_coordinates()[i], bigger_penta.get_coordinates()[i + 1]))
        bigger_penta_pairs.append((bigger_penta.get_coordinates()[4], bigger_penta.get_coordinates()[0]))
        bigger_centers = list()
        for pair in bigger_penta_pairs:
             bigger_centers.append(((pair[0][0] + pair[1][0]) / 2, (pair[0][1] + pair[1][1]) / 2))
        center_pair_list = list()
        for i in range(len(penta_pairs)):
            center_pair_list.append((penta_pairs[i], bigger_centers[i]))

        for cord in qube_cords:
            for elem in center_pair_list:
                if not self.intersect_otrezkov(elem[0][0], elem[0][1], cord, elem[1]):
                    return False
        return True