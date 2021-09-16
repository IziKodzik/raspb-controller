# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import sys
from time import sleep
from datetime import datetime
from gpiozero import Button

from gpiozero import LED, Pin, Button, DigitalInputDevice


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.g


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    button = Button(2)
    f = open('/home/pi/Desktop/work/raspb-controller/test', 'w')
    f.write('nie mozna 2?')
    print('to loopopo')
    f.close()
    s = random.randrange(2000)
    # button.when_deactivated = sys.exit
    ledW = LED(20)
    ledY = LED(21)
    while True:
        ledW.off()
        ledY.off()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
