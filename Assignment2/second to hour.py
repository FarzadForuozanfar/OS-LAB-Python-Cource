a=int(input("Enter the number in seconds  :"))

hour=a//3600

b=a-3600*hour

minute=b//60

second=b-60*minute

print(f"{hour}:{minute}:{second}")