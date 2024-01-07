from time import time


class TestDekor:

    def __init__(self):
        self.start = None

    def dekor_start(self, fanc):
        self.start = fanc

    def time_game(self, fanck):
        def wrapper(*args, **kwargs):
            start = time()
            result = fanck(*args, **kwargs)
            print(time() - start)
            return result

        self.dekor_start(wrapper)
        return wrapper
