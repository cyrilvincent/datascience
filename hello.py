import sys

print("Hello")
print(sys.version)

a = 1
b = a + 1
print(b)
print(type(b))
c = 3.14
print(type(c))

if c < 4:
    print("ok")
else:
    print("toto")

for i in range(20, 10, -2):
    print(i)

