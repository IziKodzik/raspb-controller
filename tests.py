import math
import threading
import time

import requests


class Ro:

    def __init__(self):
        self.position = [0.0, 0.0]
        self.spin = 90.
        self.xx(0, 'left')
        self.co = 0

    def nigg(self):
        t = threading.currentThread()
        while not getattr(t, "_stopped"):
            self.co += 1
            time.sleep(1)

    def go(self):
        s = threading.Thread(target=Ro.nigg, args=(self,))
        s._stopped = False
        s.start()
        for i in range(0, 3):
            print(self.co)
            time.sleep(3)
        s._stopped = True

    def xx(self, ticks, direction):

        angle = ticks * 2.5 / 280 * 360
        print(f'{angle} angle')

        c = 7 * math.sin(math.radians(90 - self.spin))
        b = 7 * math.cos(math.radians(90 - self.spin))
        print("b")
        print(c)
        print("c")
        print(b)

        if 90 < self.spin < 270:
            right_wheel_delta_x = -b
        else:
            right_wheel_delta_x = b
        if 180 < self.spin < 360:
            right_wheel_delta_y = c
        else:
            right_wheel_delta_y = -c
        print(f'{right_wheel_delta_x} delta x')
        print(f'{right_wheel_delta_y} delta y')

        if direction == 'right':
            sin = math.sin(math.radians(-angle))
            cos = math.cos(math.radians(-angle))

            self.position[0] -= right_wheel_delta_x
            self.position[1] -= right_wheel_delta_y

            nx = self.position[0] * cos - self.position[1] * sin
            ny = self.position[0] * sin + self.position[1] * cos

            self.position[0] = nx + right_wheel_delta_x
            self.position[1] = ny + right_wheel_delta_y

            print(self.position[0])
            print(self.position[1])

        else:
            left_wheel_delta_x = -right_wheel_delta_x
            left_wheel_delta_y = -right_wheel_delta_y
            sin = math.sin(math.radians(angle))
            cos = math.cos(math.radians(angle))

            self.position[0] -= left_wheel_delta_x
            self.position[1] -= left_wheel_delta_y

            nx = self.position[0] * cos - self.position[1] * sin
            ny = self.position[0] * sin + self.position[1] * cos

            self.position[0] = nx + left_wheel_delta_x
            self.position[1] = ny + left_wheel_delta_y

            print(self.position[0])
            print(self.position[1])




def d():
    pass


if __name__ == "__main__":
    r = Ro()
