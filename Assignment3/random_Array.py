

import random

array=[]
print('enter size of array:')
n=int(input())
for j in range(n):
    random_number=random.randint(0,100)
    if random_number not in array:
        array.append(random_number)

print('Array =',array)