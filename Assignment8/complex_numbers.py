from os import system
array = []
def input_data():
    a = int(input("insert real part :"))
    b = int(input("insert imaginary part :"))
    return array[a,b]

def Show_menu():
    print("""
______________________________
|                            |
|   1- + Add +               |
|   2- - Mines -             | 
|   3- x Multiply  x         |
|   4- Exit                  | 
|____________________________|""")

class Complex_numbers:
    def __init__(self, x = 0, y = 0):
        self.a = x
        self.b = y
    
    def Add(self, other):
        result = Complex_numbers(self.a + other.a,self.b + other.b)
        result.show_complx()
        return result
    
    def Mines(self, other):
        result = Complex_numbers(self.a - other.a,self.b - other.b)
        result.show_complx()
        return result
    
    def Multi(self, other):
        result = Complex_numbers()
        if self.a == 0 and other.a != 0:
            result.a = other.a
        elif self.a != 0 and other.a == 0:
            result.a = self.a
        elif self.a == 0 and other.a == 0:
            result.a = 0
        else:
            result.a = self.a * other.a 

        if self.b == 0 and other.b != 0:
            result.b = other.b
        elif self.b != 0 and other.b == 0:
            result.b = self.b
        elif self.b == 0 and other.b == 0:
            result.b = 0
        else:
            result.b = self.b * other.b
        result.show_complx()
        return result
    def show_complx(self):
        print(self.a ,"+",self.b,"i")
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ MAIn /////////////////////
while True:
    Show_menu()
    choice = int(input("insert a number from menu :"))
    if choice == 1:
        system("cls")
        print("Data for first complex number")
        input_data()
        c1 = Complex_numbers(array[0],array[1])
        array.clear()
        print("Data for first complex number")
        input_data()
        c2 = Complex_numbers(array[0],array[1])
        array.clear()
        result = Complex_numbers.Add(c1,c2)
    elif choice ==2:
        system("cls")
        print("Data for first complex number")
        input_data()
        c1 = Complex_numbers(array[0],array[1])
        array.clear()
        print("Data for first complex number")
        input_data()
        c2 = Complex_numbers(array[0],array[1])
        array.clear()
        result = Complex_numbers.Mines(c1,c2)
    elif choice == 3:
        system("cls")
        print("Data for first complex number")
        input_data()
        c1 = Complex_numbers(array[0],array[1])
        array.clear()
        print("Data for first complex number")
        input_data()
        c2 = Complex_numbers(array[0],array[1])
        array.clear()
        result = Complex_numbers.Multi(c1,c2)
    elif choice == 4:
        exit()
    else:
        print("!! command not found !!")

