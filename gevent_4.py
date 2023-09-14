import gevent.monkey

gevent.monkey.patch_socket()

import gevent
from urllib.request import urlopen
import requests
import json


def fetch(pid):
    response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow')
    result = response.text
    json_result = json.loads(result)
    datetime = json_result['datetime']

    print('Process %s: %s' % (pid, datetime))
    return json_result['datetime']


def synchronous():
    for i in range(1, 10):
        fetch(i)


def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


if __name__ == '__main__':
    print('Synchronous:')
    synchronous()

    print('Asynchronous:')
    asynchronous()
