import math
import threading
import time

import requests
class Ro:

    def __init__(self):
        self.co = 0

    def nigg(self):
        t = threading.currentThread()
        while not getattr(t, "_stopped"):
            self.co+=1
            time.sleep(1)

    def go(self):
        s = threading.Thread(target=Ro.nigg, args=(self, ))
        s._stopped = False
        s.start()
        for i in range(0, 3):
            print(self.co)
            time.sleep(3)
        s._stopped = True


def d():
    pass



if __name__ == "__main__":
    r = Ro()
    t = threading.Thread(target=d)
    r.go()
