class Person: #Classe

    def __init__(self, firstname, lastname): #Constructeur
        self.firstname = firstname #Attribut
        self.lastname = lastname

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length

if __name__ == '__main__':
    cyril = Person("Cyril","Vincent") #Instanciation
    print(cyril.firstname, cyril.lastname)
    toto = Person("Toto","Titi")
    r1 = Rectangle(3,2)
    print(r1.area(), r1.perimeter())
