import time


def timedCaller(seconds, interval, *args):

    func_array = []
    
    if not isinstance(seconds, int) or not isinstance(interval, int):
        raise TypeError("Seconds and interval must be integers")

    for func in args:
        if not callable(func):
            raise TypeError("All arguments must be callable (functions)")
        else:
            func_array = func_array.append(func)

    timer = time.time()

    while time.time() - timer < seconds:

        for func in args:
            func()
            time.sleep(interval)

    print(f"The functions {func_array} have been called for {seconds} seconds with an interval of {interval} seconds")
