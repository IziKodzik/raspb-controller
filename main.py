import curses
import threading

from Motor import Motor
from Robot import Robot


def prepare_robot():
    right_motor = Motor(18, 15, 14)
    left_motor = Motor(22, 27, 17)
    return Robot(left_motor, right_motor)


def get_dir(dee):
    print('listenin')
    while True:
        dee = stdscr.getkey()
        if ord(dee) > 0:
            print(dee == 'x')


if __name__ == '__main__':
    deer = 'p'
    stdscr = curses.initscr()
    t = threading.Thread(target=get_dir, args=deer)
    t.setDaemon(True)
    t.start()

    while deer != 'x':
        print(deer)

    print('Bye!')
