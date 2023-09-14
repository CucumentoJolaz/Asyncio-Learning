import gevent
from gevent import Timeout

seconds = 10

timeout = Timeout(seconds)
timeout.start()

def wait():
    gevent.sleep(15)
    print("Successully completed!")

try:
    gevent.spawn(wait).join()
except Timeout:
    print('Could not complete')