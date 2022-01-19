import requests
import json
import matplotlib.pyplot as plt

if __name__ == '__main__':
    api_response = requests.get('http://192.168.0.59:8080/map-points')
    print(api_response.status_code)
    data = api_response.text
    print(data)
    parse_json = json.loads(data)
    print(parse_json)
    points = list(map(lambda point: {'x': point['x'], 'y': point['y']}, parse_json))
    x = list(map(lambda point: point['x'], parse_json))
    y = list(map(lambda point: point['y'], parse_json))

    plt.rcParams["figure.figsize"] = [7.5, 7.5]
    plt.rcParams["figure.autolayout"] = True

    plt.plot(x, y, 'r*')
    plt.axis([-500, 500, -500, 500])

    plt.show()
