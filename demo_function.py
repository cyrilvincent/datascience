def add(x, y):
    return x + y


def factorielle(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """
    Retourne vrai si n est premier
    :param n: n
    :return: True si n est premier
    """
    if n < 2:
        return False
    else:
        for div in range(2, n):
            if n % div == 0:
                return False
        return True


if __name__ == '__main__':
    result = add(3, 2)
    result = add(y=2, x=3)
    print(result)
    print(factorielle(n=5))
    print(is_prime(5))

