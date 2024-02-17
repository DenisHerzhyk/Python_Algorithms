items = [
    {
        "code": 0,
        "name": "coca cola",
        "price": 5
    },
    {
        "code": 1,
        "name": "cadbury",
        "price": 10
    },
    {
        "code": 2,
        "name": "chips",
        "price": 2
    }
]

is_quit = False
item = ''
summa = 0
products = []

while is_quit is False:
    print("Welcome to the vending machine")
    for i in items:
        print(f"Item Name: {i['name']} - Price: {i['price']} - code: {i['code']}")

    query = int(input("\nEnter the code number of the item you want to get: "))

    for i in items:
        if query == i['code']:
            item = i
            summa += item["price"]
            products.append(item["name"])
    if item == '':
        print('\nINVALID CODE')

    query = input("\nTo quit the machine enter q and to continue buying enter anything: ")
    if query == 'q':
        is_quit = True
        print(f"\nGreat, total will be {summa}")

        price = int(input(f"\nEnter {summa} dollars to purchase: "))
        print("")
        if price == summa:
            for i in products:
                print(f"Thank you for buying here is your {i}")
        elif price > summa:
            for i in products:
                print(f"Thank you for buying here is your {i}")
            rest = price - summa
            print(f"\nHere is your rest - {rest}")
        else:
            print(f"\nPlease enter only {summa} dollars")
    else:
        is_quit = False
    print('')
