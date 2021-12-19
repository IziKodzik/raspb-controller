import threading
import time

import requests


def nigg():
    # t = threading.currentThread()
    # while not getattr(t, "_stopped"):
    #     print('nig')
    pass


if __name__ == "__main__":
    # s = threading.Thread(target=nigg)
    # s._stopped = False
    # s.start()
    # time.sleep(4)
    # s._stopped = True
    f = open()
    x = {'map-points':[{'x': 1, 'y': 2},
                              {'x': 1, 'y': 2},
                              {'x': 1, 'y': 2},
                              {'x': 1, 'y': 2},
                              {'x': 1, 'y': 2},
                              ]}
    x['map-points'].append(   {'x': 1, 'y': 69})
    res = requests.post("http://localhost:8080/map-points",
                        json=x)
    print(res.text)
    pass
