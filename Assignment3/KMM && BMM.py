
num1 = int (input ("Enter firs number : "))
num2 = int (input ("Enter second number : "))

for i in range (1, num1 + 1):
	if i <= num2:
		if num1 % i == 0 and num2 % i == 0:
			BMM = i

KMM = int((num1 * num2) / BMM)
print("\nKMM is :",KMM,"\nBMM is:",BMM)