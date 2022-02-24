print("Enter a number = ")
number = input()
n =int(number)
count = 1
sum = 0

while n >= 10: #digits of a number
        n = n / 10
        count += 1


for digit in number:
    sum += int(digit) ** count
 
if(sum == int(number)):
    print("yes")
else:
    print("no")