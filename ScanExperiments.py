import math
import os

import numpy as np
import requests
import json
import matplotlib.pyplot as plt

from Point import Point


def xx():
    api_response = requests.get('http://192.168.0.59:8080/map-points')
    data = api_response.text
    parse_json = json.loads(data)

    points = list(map(lambda point: Point(point['x'], point['y'], point['angle']), parse_json))
    if len(points) <= 1:
        return 1

    points.sort(key=lambda key: key.angle)
    current_angle = calc_angle(points[0], points[1])
    print(current_angle)

    last_avg = current_angle
    lx = []
    ly = []

    for i in range(1, len(points)-1):
        point_counter = 0
        examined_point = points[i]
        angle_sum = 0
        try:
            next_point = points[i + 1]
            for j in range(1, 6):
                sub_point = points[i + j]
                sub_angle = calc_angle(examined_point, sub_point)
                angle_sum += sub_angle
                point_counter += 1
            if point_counter == 0:
                point_counter = 1
        except IndexError:
            pass
        if point_counter == 0:
            point_counter = 1
        avg_angle = angle_sum / point_counter
        if abs(avg_angle - last_avg) > 20:
            lx.append(examined_point.x)
            ly.append(examined_point.y)
        last_avg = avg_angle
        print(avg_angle)


    x = list(map(lambda point: point['x'], parse_json))
    y = list(map(lambda point: point['y'], parse_json))

    plt.rcParams["figure.figsize"] = [7.5, 7.5]
    plt.rcParams["figure.autolayout"] = True

    plt.plot(x, y, 'b.')
    plt.plot(lx, ly, 'rx')
    # plt.show(lx, ly, 'rx')
    # plt.plot(points[0].x, points[0].y, 'rx')
    # plt.plot(points[1].x, points[1].y, 'rx')
    plt.axis([-500, 500, -500, 500])

    plt.show()


def calc_angle(point0, point1):
    dx = point0.x - point1.x
    dy = point0.y - point1.y
    angle = math.degrees(math.atan((point0.y - point1.y) / (point0.x - point1.x + 0.00000000000000001)))
    if dx > 0 and dy < 0 or (dx > 0 and dy > 0):
        angle += 180
    if dx < 0 and dy > 0:
        angle = 360 + angle
    return angle

def calc_dist(point0, point1):
    dx = (point0.x - point1.x)
    dy = (point0.y - point1.y)
    return math.sqrt(
        dx ** 2 + dy ** 2) + 0.0000000000000000000000000000000000000000000000000000000000000000000000000000000001

# def calc_angle22(point0, point1):
#     dx = (point0.x - point1.x)
#     dy = (point0.y - point1.y)
#     dp = math.sqrt(
#         dx ** 2 + dy ** 2) + 0.0000000000000000000000000000000000000000000000000000000000000000000000000000000001
#
#     sin = dy / dp
#     cos = dx / dp
#
#     return math.degrees(np.angle(cos + 1j * sin))


if __name__ == '__main__':
    # print(calc_angle(Point(0, 0, 2), Point(1, 0.02, 2)))
    # print(calc_angle(Point(0, 0, 2), Point(-1, 0.02, 2)))
    # print(calc_angle(Point(0, 0, 2), Point(-0.001, -1, 2)))
    # print(calc_angle(Point(0, 0, 2), Point(0.01, -1, 2)))
    xx()
#
