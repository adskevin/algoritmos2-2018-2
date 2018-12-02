# Espaco.py

import random


class Estrela:

    def __init__(self):
        self.x = 800
        self.y = random.randint(0, 600)
        self.x_old = self.x
        self.y_old = self.y
        self.spd = random.randint(1, 3)
        self.spd_old = self.spd
        self.alive = True

    def set_vel(self, vel):
        # global spd
        if vel >= 0 and vel <= 3:
            self.spd = vel

    def set_coord_x(self, coord_x):
        # global x
        if coord_x >= 0 and coord_x <= 800:
            self.x = coord_x
        elif coord_x < 0:
            self.x = 0

    def set_coord_y(self, coord_y):
        # global y
        if coord_y >= 0 and coord_y <= 600:
            self.y = coord_y
        elif coord_y < 0:
            self.y = 0

    def move_estrela(self):
        if self.x >= 0 and self.x <= 800:
            self.x = self.x - self.spd
        if self.x < 0 or self.x > 800:
            self.alive = False

    def get_x(self):
        return self.x

    def get_y(self):
        # global y
        return self.y

    def get_vel(self):
        # global spd
        return self.spd
