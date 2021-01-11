import sys
import mylib as toto

def is_even():
    pass

print("Hello World")
print(sys.version)
print(toto.is_even(7))

l1 = [1,2,3,4]
l2 = l1
l2.append(5)
print(l1, l2)
print(l1 == l2)
print(l1 is l2)

l1 = [1,2,3,4]
l2 = list(l1)
l1.append(5)
l2.append(5)
print(l1, l2)
print(l1 == l2)
print(l1 is l2)
print(type(l1))

