from typing import List

def is_even(x:int):
    return x % 2 == 0

def is_prime(x:int):
    pass
    # Est divisible par lui même et 1

def filter_even(l:List[int]):
    res = []
    for i in l:
        if is_even(i):
            res.append(i)
    return res

def filter_prime(l:List[int]):
    pass



if __name__ == '__main__':
    print(is_even(8))
    print(filter_even(range(10000000)))