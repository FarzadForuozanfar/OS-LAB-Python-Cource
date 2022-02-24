IsTriangle = True
a = float(input("Enter number 1 :"))
b = float(input("Enter number 2 :"))
c = float(input("Enter number 3 :"))
if (a + b < c) :
    IsTriangle = False
if(c + b < a ):
    IsTriangle = False
if(c + a < b ):
    IsTriangle = False
if (IsTriangle):
    print("we can make Triangle")
else:
    print("we cant make Triangle")

