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


print(is_prime(7), is_prime(9))