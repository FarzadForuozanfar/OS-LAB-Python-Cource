import os

Prodacts =[]

def read_from_database():
    f = open('database.txt', 'r')
    text = f.read()
    rows = text.split("\n")
    for row in rows:
        info = row.split(",")
        new_dict = {'code':info[0], 'name':info[1], 'price':info[2], 'count':info[3]}
        Prodacts.append(new_dict)
        

def show_list():
    os.system("clear")
    read_from_database()
    for prodact in Prodacts:
        print([prodact])

def add():
    os.system("clear")
    code = input("Enter code for new product: ")
    name = input("Enter name for new product: ")
    price = input("Enter price for new product: ")
    count = input("Enter count for new product: ")
    Prodacts.append({"code":code,"name":name,"price":price,"count":count})

def delete():
    temp_name = input("Enter the name of the product you want to delete: ")
    for prodact in Prodacts:
        if prodact["name"] == temp_name:
            Prodacts.remove[prodact]
            print("The product was deleted")
            break
        else:
            print("product not found")
    return

def edit():
    name = input("Enter the name of the product you want to edit: ")
    for prodact in Prodacts:
        if name == Prodacts[prodact]:
            new_name = input("enter new name for product: ")
            Prodacts[prodact]['name'] = new_name
            new_code = input("enter new code for product: ")
            Prodacts[prodact]['code'] = new_code
            new_price = input("enter new price for product: ")
            Prodacts[prodact]['price'] = new_price
            new_count = input("enter new count for product: ")
            Prodacts[prodact]['count'] = new_count

    else:
            print("product not found")
        
def search():
    search_name = input("Enter the name of the product you want to search: ")
    for product in Prodacts:
        if Prodacts[product]['name'] == search_name:
            print("this product is exist in store")
            print(Prodacts[product]["name"],Prodacts[product]["code",Prodacts[product]["price"],Prodacts[product]["count"]])
            return
    else:
        print("product not found in list")

def buy():
    product_name =[]
    shoping_list = []
    cost_list_shop = []
    for product in Prodacts:
        product_name.append(Prodacts[product]['name'])
    flag = True
    while flag:
        x = 1
        print("enter the product name you are looking for ((for example:milk)) :")
        for i in product_name:
            print(x,"- ",product_name[i],"\n")
            x += 1
        print(x,"- Exit the shopping list and transfer to the payment page")
        select = input()
        if select == 'Exit' or 'exit':
            break
        else:
            digit_product_shop = input("Enter number of",product_name[i])
            cost_list_shop.append(digit_product_shop * product_name[i]['price'])
        total_cost = 0
    for i in  cost_list_shop:
        total_cost += cost_list_shop[i]
    print("Total cost for paid is: ",total_cost)


def save():
    f = open('database.txt', 'r')
    text = f.write(Prodacts)

def show_menu():
    print("""1- Add
2- Edit
3- Delete
4- Show List
5- Search
6- Buy
7- Exit""")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ MAIN ////////////////////////////#
while True:
    show_menu()
    choose = input("select your choice :")
    if choose == 1:
        add()
    elif choose == 2:
        edit()
    elif choose == 3:
        delete()
    elif choose == 4:
        show_list()
    elif choose == 5:
        search()
    elif choose == 6:
        buy()
    elif choose == 7:
        save()
        exit()

