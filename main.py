import select

from Motor import Motor
import sys, pygame
import curses
import termios
import tty


def isData():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def met():
    if c == ord('w'):
        right_motor.go_forward()
        left_motor.go_forward()

    elif c == ord('s'):
        right_motor.go_backward()
        left_motor.go_backward()
    elif c == ord('a'):
        right_motor.go_backward()
        left_motor.go_forward()
    elif c == ord('d'):
        left_motor.go_backward()
        right_motor.go_forward()
    else:
        right_motor.go_with_speed(0)
        left_motor.go_with_speed(0)


if __name__ == '__main__':
    print('controller running')
    stdscr = curses.initscr()
    curses.noecho()
    stdscr.nodelay(True)
    right_motor = Motor(18, 15, 14)
    left_motor = Motor(22, 27, 17)

    old_settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())

        while True:
            c = stdscr.getch()



    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
