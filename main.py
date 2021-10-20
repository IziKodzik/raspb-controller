
import curses

from Motor import Motor
from Robot import Robot


def prepare_robot():
    right_motor = Motor(18, 15, 14)
    left_motor = Motor(22, 27, 17)
    return Robot(left_motor, right_motor)


if __name__ == '__main__':
    stdscr = curses.initscr()
    while True:
        x = stdscr.getkey()
        if ord(x) > 0:
            print('You pressed the', x, 'key.')
        print('negro')
        if x == 27:
            break

    print('Bye!')