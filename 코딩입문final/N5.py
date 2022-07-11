menu_list = ["coffee","latte","tea"]
order = []
total_price = None

def inputDrink():
    tmp_menu = input("메뉴) coffee, latte, tea 중에 선택:")
    menu_in_list = False

    for i in menu_list:
        if tmp_menu == i:
            menu_in_list = True

    if not menu_in_list:
        exit(0)
    return tmp_menu

def returnPrice(drink):
    if drink == "coffee":
        return int(2500)
    elif drink == "latte":
        return int(3000)
    elif drink == "tea":
        return int(3000)


def inputCount():
    return int(input("해당 메뉴 갯수)"))


def printResult(drink, price, count):
    order_list = [drink, price]
    order.append(order_list)
    total_price = count * price
    print("주문내역:", order_list)
    print("주문총액:", total_price)

def foodChoicer():
    while True:
        accept_order = input("주문하실래요? yes/no")
        if accept_order == "yes":
            drink = inputDrink()
            printResult(drink, returnPrice(drink), inputCount())
        else:
            break


foodChoicer()