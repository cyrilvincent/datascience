import demo_function as f

print(f.factorielle(5))

print("Hello")

# Factorielle
n = 5
result = 1
for i in range(2,n + 1):
    result *= i
print(result)

# Pairs * 2, impairs / 2
for i in range(10):
    if i % 2 == 0:
        print(i * 2)
    else:
        print(i / 2)

is_prime = True
n = 7919
for div in range(2, n):
    if n % div == 0:
        is_prime = False
        break
print(is_prime)
