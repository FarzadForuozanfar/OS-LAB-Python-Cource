size = int(input('Enter a number for size of fibo: '))

fibo = [0, 1]
if size == 1:
    print(fibo[0])
else:
    for i in range(2, size):
        fibo.append(fibo[i - 1] + fibo[i - 2])
        print("fibo[",i,"]=",fibo[i])