import gevent
import signal

def run_forever():
    gevent.sleep(1000)

if __name__ == '__main__':
    gevent.signal_handler(signal.SIGINT, gevent.kill)
    thread = gevent.spawn(run_forever)
    thread.join()