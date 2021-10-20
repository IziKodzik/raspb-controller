import curses
import threading

from Motor import Motor
from Robot import Robot


def prepare_robot():
    right_motor = Motor(18, 15, 14)
    left_motor = Motor(22, 27, 17)
    return Robot(left_motor, right_motor)


def get_dir():
    while True:
        dir = stdscr.getkey()
        if ord(dir) > 0:
            print('You pressed the', dir, 'key.')


if __name__ == '__main__':
    global dir
    dir = 'p'
    stdscr = curses.initscr()
    t = threading.Thread(target=get_dir)
    t.setDaemon(True)
    t.start()

    while True:
        if dir == 'x':
            break
        print('negro')

    print('Bye!')
