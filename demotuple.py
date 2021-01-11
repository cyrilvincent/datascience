def min_max_avg(l):
    return 0,99,50

def min_max_avg_dico(l):
    return {"min":0,"max":99,"avg":50}

def per_tuple(*kargs):
    for param in kargs:
        print(param)

def per_dict(**kwargs):
    print(kwargs)
    for param in kwargs.keys():
        print(param)
        print(kwargs[param])

def the_bordel(a,*kargs,**kwargs):
    print(a)
    print(kargs)
    print(kwargs)

if __name__ == '__main__':
    min, max, avg = min_max_avg(range(100))
    print(min, max, avg)
    dico = min_max_avg_dico(range(100))
    print(dico["min"])
    per_tuple(1,4,5,6,99)
    per_dict(toto=1, titi=4)
    the_bordel(1,2,3,4,5,toto=1, titi=4)
    
