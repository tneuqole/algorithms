from input import gen_arr
import math

input = gen_arr(1000)
input.sort()


def binary_search(input: list[int], target: int) -> int:
    start = 0
    end = len(input) - 1
    while start <= end:
        idx = int(math.floor((start + end) / 2))
        if input[idx] < target:
            start = idx + 1
        elif input[idx] > target:
            end = idx - 1
        else:
            return idx

    return None


res = binary_search(input, input[260])
assert res == 260
