from time import sleep

from gpiozero import DistanceSensor

from Motor import Motor
from Robot import Robot


def prepare_robot():
    right_motor = Motor(18, 15, 14)
    left_motor = Motor(22, 27, 17)
    return Robot(left_motor, right_motor)


if __name__ == '__main__':
    collision_sensor = DistanceSensor(echo=23, trigger=24)
    while True:
        print(collision_sensor.distance * 100)
        sleep(1)
