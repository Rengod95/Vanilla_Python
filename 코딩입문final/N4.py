# def foodChoicer():
#     pass


def inputDrink():
    return input("메뉴) coffee, latte, tea 중에 선택:")

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
    order_list = [drink,price]
    print("주문내역:", order_list)
    print("주문총액:", count*price)


drink = inputDrink()
printResult(drink, returnPrice(drink), inputCount())
