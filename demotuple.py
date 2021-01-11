def min_max_avg(l):
    min = l[0]
    max = l[0]
    sum = 0
    for i in l:
        if i < min:
            min = i
        elif i > max:
            max = i
        sum += i
    return min, max, sum/len(l)


def min_max_avg_dico(l):
    min = l[0]
    max = l[0]
    sum = 0
    for i in l:
        if i < min:
            min = i
        if i > max:
            max = i
        sum += i
    return {"min": min, "max": max, "avg": sum/len(l)}


def per_tuple(*kargs):
    for param in kargs:
        print(param)


def per_dict(**kwargs):
    print(kwargs)
    for param in kwargs.keys():
        print(param)
        print(kwargs[param])


def the_bordel(a, *kargs, **kwargs):
    print(a)
    print(kargs)
    print(kwargs)


if __name__ == '__main__':
    min, max, avg = min_max_avg(range(100))
    print(min, max, avg)
    dico = min_max_avg_dico(range(100))
    print(dico["min"])
    per_tuple(1, 4, 5, 6, 99)
    per_dict(toto=1, titi=4)
    the_bordel(1, 2, 3, 4, 5, toto=1, titi=4)

