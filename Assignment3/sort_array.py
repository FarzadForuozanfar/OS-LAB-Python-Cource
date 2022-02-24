from typing import Counter


size_array = int(input("insert size of array :"))
Counter = 0
numbers = []
is_sort = True
while Counter < size_array:
    x = int(input())
    numbers.append(x)
    Counter += 1
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] > numbers[j]:
                is_sort = False
    if is_sort == True:
        print("yes its sort")

    else:
        print("no it isnt sort")
