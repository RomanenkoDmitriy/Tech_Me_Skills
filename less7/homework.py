import time


def time_work(fanc):
    stat = time.time()

    def wrapper(*args):
        # stat = time.time()
        res = fanc(*args)
        # r = time.time() - stat
        # print(args, r)
        return res

    time_res = time.time() - stat
    print(f"Dekor {time_res}")
    return wrapper


@time_work
def fib(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * fib(n - 1)


if __name__ == '__main__':
    print(fib(5))
