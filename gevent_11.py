import gevent
from gevent.event import AsyncResult
a = AsyncResult()

def setter(add_int):
    """
    After 3 seconds set the result of a.
    """
    gevent.sleep(3)
    out_int = 3 + add_int
    a.set(out_int)

def waiter():
    """
    After 3 seconds the get call will unblock after the setter
    puts a value into the AsyncResult.
    """
    print(a.get())

gevent.joinall([
    gevent.spawn(setter, 3),
    gevent.spawn(waiter),
])