import random


def gen_arr(n: int) -> list[int]:
    return [int(random.random() * n) for i in range(n)]
