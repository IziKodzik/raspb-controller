import select

from Motor import Motor
import sys, pygame
import termios
import tty


def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


if __name__ == '__main__':
    print('controller running')
    pygame.init()
    right_motor = Motor(18, 15, 14)
    left_motor = Motor(22, 27, 17)

    old_settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())

        while True:
            c = 0
            if isData():
                c = sys.stdin.read(1)
                print(c)


    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
