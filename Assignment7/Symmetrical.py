def Print_KHoshgelasion(number):
    number = str(number + 1)
    string = "insert Array[" +number+"] = "
    return string

def Is_Symmetrical(array, size):
    symmetrical = True
    cnt_roll_back = len(array) - 1
    for i in range(size):
        if array[i] != array[cnt_roll_back]:
            symmetrical = False
        cnt_roll_back -= 1
    return symmetrical

SIZE = int(input("Please insert size of Array ="))
array = []
for i in range(SIZE):
    array.append(int(input(Print_KHoshgelasion(i))))
if not Is_Symmetrical(array, SIZE) or SIZE % 2 == 0:
    print("⛔️❌ No it isnt symmetrical ❌⛔️")
    
else:
    print("💚✅ Yes its symmetrical ✅💚")