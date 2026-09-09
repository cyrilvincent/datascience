n = 5
# 1*2*3*4*5
# n!
result = 1
for i in range(2, n+1):
    result *= i

print(f"{n}!={result}")


n=1499
# n est il premier : 7 est divisible que par 1 et 7
# Tout nombre > 1 est premier SAUF s'il possède un diviseur entre 2 et n-1
if n < 2:
    print("Non premier")
else:
    is_prime = True
    for div in range(2, n):
        if n % div == 0:
            is_prime = False
            break
    if is_prime:
        print("Premier")
    else:
        print("Non premier")
