
from os import system
list_num = []
def lcm(num1 , num2):
    a = num1
    b = num2
    if a < b:
        temp = a
        a = b
        b = temp
    while b != 0:
        r = a % b
        a = b
        b = r
    return int((num1 * num2) / a)
def input_date():
    num1 = int(input("Plz Enter numerator  :"))
    num2 = int(input("Plz Enter denominator  :"))
    while num2 == 0:
        print("!! The denominator of the fraction cannot be entered as zero !!")
        num2 = int(input("!!Try Again!! Enter denominator :"))
    list_num.append(num1)
    list_num.append(num2)
    return list_num
def Show_menu():
    print("""
______________________________
|                            |
|   1- + ADD Fraction +      |
|   2- - Mines Fraction -    | 
|   3- x Multiply x          |
|   4- / Division /          |
|   5- EXIT                  |   
|____________________________|""")
class Fraction_Math:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom
    def Add(self, other):
        denom_result = lcm(self.denominator, other.denominator)
        print(int(denom_result / other.denominator),int(denom_result / self.denominator))
        result = (self.numerator * int(denom_result / self.denominator) + other.numerator * int(denom_result / other.denominator), denom_result)
        return result
    def Sub(self, other):
        denom_result = lcm(self.denominator, other.denominator)
        result = (self.numerator * int(denom_result / self.denominator) + other.numerator * int(denom_result / other.denominator), denom_result)
        return result
    def Mul(self, other):
        return self.numerator*other.numerator, self.denominator*other.denominator
    def Div(self, other):
        return self.numerator*other.denominator, self.denominator*other.numerator
    def Show_Fraction_Math(self):
        return '%s/%s' %(self.numerator, self.denominator)
    def __str__(self):
        if type(self) is tuple:
            if self[1] < 0:
                return '%s/%s' %(self[0], -1*self[1])
            else:
                return '%s/%s' %(self[0], self[1])
        elif self.denominator == 1:
            return str(self.numerator)
        else:
            return '%s/%s' %(self.numerator, self.denominator)
#///////////////////////////////////////////////// MAIN \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#while True:
while True:
    
    Show_menu()
    SELECT = int(input("Select your choice: "))
    if SELECT == 1:
        system('clear')
        print(" Data of first Fraction ")
        input_date()
        FRC1 = Fraction_Math(list_num[0],list_num[1])
        list_num.clear()
        print(" Data of second Fraction ")
        input_date()
        FRC2 = Fraction_Math(list_num[0],list_num[1])
        list_num.clear()
        Result = Fraction_Math.Add(FRC1,FRC2)
        print(Fraction_Math.__str__(FRC1), " + ", Fraction_Math.__str__(FRC2)," = ",Fraction_Math.__str__(Result))
    elif SELECT == 2:
        system('clear')
        print(" Data of first Fraction ")
        input_date()
        FRC1 = Fraction_Math(list_num[0],list_num[1])
        list_num.clear()
        print(" Data of second Fraction ")
        input_date()
        FRC2 = Fraction_Math(list_num[0],list_num[1])
        list_num.clear()
        Result = Fraction_Math.Add(FRC1,FRC2)
        print(Fraction_Math.__str__(FRC1), " - ", Fraction_Math.__str__(FRC2)," = ",Fraction_Math.__str__(Result))
    elif SELECT == 3:
        system('clear')
        print(" Data of first Fraction ")
        input_date()
        FRC1 = Fraction_Math(list_num[0],list_num[1])
        list_num.clear()
        print(" Data of second Fraction ")
        input_date()
        FRC2 = Fraction_Math(list_num[0],list_num[1])
        list_num.clear()
        Result = Fraction_Math.Add(FRC1,FRC2)
        print(Fraction_Math.__str__(FRC1), " X ", Fraction_Math.__str__(FRC2)," = ",Fraction_Math.__str__(Result))
    elif SELECT == 4:
        system("clear")
        print(" Data of first Fraction ")
        input_date()
        FRC1 = Fraction_Math(list_num[0],list_num[1])
        list_num.clear()
        print(" Data of second Fraction ")
        input_date()
        FRC2 = Fraction_Math(list_num[0],list_num[1])
        list_num.clear()
        Result = Fraction_Math.Add(FRC1,FRC2)
        print(Fraction_Math.__str__(FRC1), " / ", Fraction_Math.__str__(FRC2)," = ",Fraction_Math.__str__(Result))
    elif SELECT == 5:
        exit()
        break