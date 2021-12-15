import threading
import time


def nigg():
    t = threading.currentThread()
    while not getattr(t, "_stopped"):
        print('nig')

if __name__ == "__main__":
    s = threading.Thread(target=nigg)
    s._stopped = False
    s.start()
    time.sleep(4)
    s._stopped = True
