while True:
    n = int(input("Enter number for row :"))
    m = int(input("Enter number for column :"))
    if n > 0 and m > 0:
        break
for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                if j % 2 == 0:
                    print('#', end='')
                else:
                    print('*', end='')
            else:
                if j % 2 == 0:
                    print('*', end='')
                else:
                    print('#', end='')
        print()

