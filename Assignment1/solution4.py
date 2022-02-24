height = float(input("Enter Ur height :"))
weight = float(input("Enter Ur weight :"))
if(weight/(height*height) <= 18.5):
    print("you are UnderWeight ")
elif(18.5 < weight/(height*height) <= 24.9):
    print("you are Normal ")
elif(25 < weight/(height*height) <= 29.9):
    print("you are OverWeight ")
elif(30 < weight/(height*height) <= 34.9):
    print("you are Obese ")
elif(weight/(height*height) > 35):
    print("you are ExtranllyObese ")

