def add(x, y):
    return x + y


print(add(2, 3))
print(add(x=2, y=3))


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for div in range(2, n):
        if n % div == 0:
            return False
    return True

f = lambda x, y: x + y
print(f(2,3))

f = lambda x: x + 1
print(f(1))
