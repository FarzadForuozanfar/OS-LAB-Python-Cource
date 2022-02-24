import math
while True:
    print("1- Add two number")
    print("2- Mines two number")
    print("3- Multiply two number")
    print("4- Divided two number")
    print("5- Sinus of an angle")
    print("6- Cosinus of an angle")
    print("7- Tangent of an angle")
    print("8- Cotangent of an angle")
    print("9- logarithm a number")
    print("10- exit program")
    Opration = input()
    if(Opration == '1'):
        print("Enter  number 1 for calculate")
        number_1 = float(input())
        print("Enter  number 2 for calculate")
        number_2 = float(input())
        print(number_1," + ",number_2," = ",number_2 + number_1)
    elif(Opration == '2'):
        print("Enter  number 1 for calculate")
        number_1 = float(input())
        print("Enter  number 2 for calculate")
        number_2 = float(input())
        print(number_1," - ",number_2," = ",number_1 - number_2)
    elif(Opration == '3'):
        print("Enter  number 1 for calculate")
        number_1 = float(input())
        print("Enter  number 2 for calculate")
        number_2 = float(input())
        print(number_1," x ",number_2," = ",number_2 * number_1)
    elif(Opration == '4'):
        print("Enter  number 1 for calculate")
        number_1 = float(input())
        print("Enter  number 2 for calculate")
        number_2 = float(input())
        print(number_1," / ",number_2," = ",number_1 / number_2)
    elif(Opration == '5'):
        print("Enter a Angle for calculat")
        angle = float(input())
        degree = angle/360 *2 *math.pi
        result = math.sin(degree)
        print("sin ",angle," = ",result)
    elif(Opration == '6'):
        print("Enter a Angle for calculat")
        angle = float(input())
        degree = angle/360 *2 *math.pi
        result = math.cos(degree)
        print("cos ",angle," = ",result)
    elif(Opration == '7'):
        print("Enter a Angle for calculat")
        angle = float(input())
        degree = angle/360 *2 *math.pi
        result = math.tan(degree)
        print("tan ",angle," = ",result)
    elif(Opration == '8'):
        print("Enter a Angle for calculat")
        angle = float(input())
        degree = angle/360 *2 *math.pi
        result = math.sin(degree)
        print("cot ",angle," = ",result)
    elif(Opration == '9'):
        print("Enter a number for calculat")
        number = float(input())
        print("log (",number,") = ",math.log(number))
    elif(Opration == '10'):
        break
    else:
        print("command not found")
