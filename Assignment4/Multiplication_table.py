while True:
    n = int(input("Enter number for row :"))
    m = int(input("Enter number for column :"))
    if n > 0 and m > 0:
        break

for i in range(1,n+1):
    for j in range(1,m+1):
       print("[",i,"x",j,"=",i*j,"]",end=" ")
    print()