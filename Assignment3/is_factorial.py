number = int(input('Enter your Number: '))
n = 0
i = 0
while n < number:
    i += 1
    n *= i
if number == n:
    print('Yes')
else:
    print('No')


