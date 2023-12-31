import gevent
from gevent import Greenlet

def foo(message, n):
    """
    Each thread will be passed the message, and n arguments
    in its initialization.
    """
    gevent.sleep(n)
    print(message)

# Initialize a new Greenlet instance running the named function
# foo
thread1 = Greenlet.spawn(foo, "Hello", 5)

# Wrapper for creating and running a new Greenlet from the named
# function foo, with the passed arguments
thread2 = gevent.spawn(foo, "I live!", 1)

# Lambda expressions
thread3 = gevent.spawn(lambda x: print(x+10), 70)

threads = [thread1, thread2, thread3]

# Block until all threads complete.
gevent.joinall(threads)
print("Работаю после!")
