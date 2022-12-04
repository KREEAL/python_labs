import math
from Pentagon import Pentagon


class Quad:
    def __init__(self, name, side, x, y):
        self.name = name
        try:
            if side <= 0:
                side = 0
                side = side / side
            self.side = side
        except ZeroDivisionError:
            print('Ошибка создания фигуры. Выбрано базовое значение = 42')
            self.side = 42
        self.center_x = x
        self.center_y = y
        self.coords = [(self.center_x - self.side / 2, self.center_y + self.side / 2),
                       (self.center_x + self.side / 2, self.center_y + self.side / 2),
                       (self.center_x + self.side / 2, self.center_y - self.side / 2),
                       (self.center_x - self.side / 2, self.center_y - self.side / 2)]

    def initiate_coordinates(self) -> list:
        self.coords = [(self.center_x - self.side / 2, self.center_y + self.side / 2),
                       (self.center_x + self.side / 2, self.center_y + self.side / 2),
                       (self.center_x + self.side / 2, self.center_y - self.side / 2),
                       (self.center_x - self.side / 2, self.center_y - self.side / 2)]

    def rotate(self, alfa):
        self.initiate_coordinates()
        alfa = alfa * math.pi / 180
        for i in range(4):
            x = self.coords[i][0] * math.cos(alfa) - self.coords[i][1] * math.sin(alfa)
            y = self.coords[i][0] * math.sin(alfa) + self.coords[i][1] * math.cos(alfa)
            self.coords[i] = (x, y)

    def get_coordinates(self) -> list:
        self.initiate_coordinates()
        return self.coords

    def move(self, x, y):
        self.center_x = self.center_x + x
        self.center_y = self.center_y + y
        self.initiate_coordinates()

    def rotate_tochki(self, a, b, c):
        return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])

    def intersect_otrezkov(self, a, b, c, d):
        return self.rotate_tochki(a, b, c) * self.rotate_tochki(a, b, d) <= 0 and self.rotate_tochki(c, d,
                                                                                                     a) * self.rotate_tochki(
            c, d, b) < 0

    def is_intersect(self, penta: Pentagon):
        penta_cords = penta.get_coordinates()
        qube_pairs = list()
        for i in range(3):
            qube_pairs.append((self.coords[i], self.coords[i + 1]))
        qube_pairs.append((self.coords[3], self.coords[0]))
        print(qube_pairs)

        bigger_quad = Quad('temp', self.side * 1.1, self.center_x, self.center_y)
        bigger_quad.rotate(15)
        bigger_quad_pairs = list()
        for i in range(3):
            bigger_quad_pairs.append((bigger_quad.get_coordinates()[i], bigger_quad.get_coordinates()[i + 1]))
        bigger_quad_pairs.append((bigger_quad.get_coordinates()[3], bigger_quad.get_coordinates()[0]))

        bigger_centers = list()
        for pair in bigger_quad_pairs:
            bigger_centers.append(((pair[0][0] + pair[1][0]) / 2, (pair[0][1] + pair[1][1]) / 2))

        center_pair_list = list()
        for i in range(len(qube_pairs)):
            center_pair_list.append((qube_pairs[i], bigger_centers[i]))

        for cord in penta_cords:
            for elem in center_pair_list:
                if not self.intersect_otrezkov(elem[0][0], elem[0][1], cord, elem[1]):
                    return False
        return True
