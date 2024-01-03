"""
Написать декоратор который будет сохранять(кешировать) результат выполнения любой ф-ции,
то есть, в первый раз ф-ция с одними и теми же параметрами будет запускаться
а во все остальные разы с теми же параметрами результат будет возвращаться из кеша.

доп: добавить время жизни кеша, например 15 секунд.
"""
import json

from datetime import datetime, timedelta


res_dict = {}


def dec_hash(tim: int):
    def dec(fanc):
        def wrapper(arg):

            if arg in res_dict:
                res = res_dict[arg][0]
                return res
            else:
                res = fanc(arg)
                res_dict[arg] = [res, datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")]
                with open("cash.json", "w") as file:
                    json.dump(res_dict, file)

                return res

        return wrapper
    return dec


@dec_hash(20)
def calk(arg: str) -> int:
    return eval(arg)


if __name__ == "__main__":

    inp = input("Введите выражение  без пробелов: ").strip()

    while inp != "":

        print(calk(inp))
        inp = input("Введите выражение без пробелов: ").strip()
        print(res_dict)
