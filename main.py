# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
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
    f = open('/home/pi/Desktop/work/raspb-controller/test', 'a')
    f.write('cki')
    f.close()
    button = Button(2)
    button.wait_for_inactive()
    print('to loop')
    while not button.is_active:
        f.write(f'{datetime.now()}')
        f.close()
        sleep(10)
    print('finito')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
