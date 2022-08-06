import requests


def work():
    url = "http://www.boredapi.com/api/activity/"
    json = (requests.get(url=url)).json()

    return json['activity']
