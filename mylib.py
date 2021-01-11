from typing import List
import math


def is_even(x:int):
    return x % 2 == 0


def is_prime(x:int):
    if x < 2:
        return False
    else:
        for div in range(2, int(math.sqrt(x)) + 1):
            if x % div == 0:
                return False
        return True


def filter_even(l: List[int]):
    res = []
    for i in l:
        if is_even(i):
            res.append(i)
    return res


def filter_prime(l: List[int]):
    res = []
    for i in l:
        if is_prime(i):
            res.append(i)
    return res


def filter_generic(l: List[int], fn):
    res = []
    for i in l:
        if fn(i):
            res.append(i)
    return res

def double(x):
    return x * 2

def map_generic(l: List[int], fn):
    res = []
    for i in l:
        res.append(fn(i))
    return res


if __name__ == '__main__':
    print(is_even(8))
    #print(filter_even(range(100)))
    print(is_prime(7))
    print(is_prime(11587))
    #print(filter_prime(range(100)))
    print(filter_generic(range(100), fn=lambda x : x % 2 == 0))
    print(list(filter(lambda x : is_prime(x), range(100))))
    print(map_generic(range(100),fn=lambda x: x * x))
    print(list(map(lambda x: x * x, range(100))))
    # fn = is_even
    # print(type(fn))
    # print(fn(8))
    # Filtrer 2 fois range(100) pour trouver le nombre premier pair

    res = filter(lambda x : x % 2 == 0, range(100))
    res = filter(lambda x : is_prime(x), res)
    print(list(res))

    print(list(map(lambda x : x**2, filter(lambda x : is_prime(x), range(100)))))
    print([x ** 2 for x in range(100) if is_prime(x)])
