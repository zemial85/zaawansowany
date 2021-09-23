from datetime import datetime


def how_long_it_takes(func):
    def wrapper():
        print(func)
        before_calling = datetime.now()
        returns = func()
        after_calling = datetime.now()
        print(after_calling - before_calling)
        return returns

    return wrapper


@how_long_it_takes
def slow_proc():
    print("something is happening")
    a = [x for x in range(50000000)]

slow_proc()