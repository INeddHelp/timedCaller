import time


def timedCaller(seconds, interval, *args):

    if not isinstance(seconds, int) or not isinstance(interval, int):
        raise TypeError("Seconds and interval must be integers")

    for func in args:
        if not callable(func):
            raise TypeError("All arguments must be callable (functions)")

    timer = time.time()

    while time.time() - timer < seconds:

        if interval != 0:
            for func in args:
                func()
                time.sleep(interval)
        else:
            for func in args:
                func()

    print(f"Timer with {seconds} seconds has finished.")
