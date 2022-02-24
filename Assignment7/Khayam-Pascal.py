def khayampascal(n):
    array=[]
    end = n
    for n in range(0,n):
        array.append([])
        if n==0:
            array[n].append(1)
        elif n==1:
            array[n].append(1)
            array[n].append(1)
        elif n>=2 and n<end:
            array[n].append(1)
            for i in range(1,n):
                array[n].append(array[n-1][i]+array[n-1][i-1])
            array[n].append(1)
    return array

def printmatrix(array):
    for entry in array:
        print(entry)
    print('')

num = int(input('Please enter a number:'))
printmatrix(khayampascal(num))
