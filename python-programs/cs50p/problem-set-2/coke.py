def main():
    coke_price = 50
    while True:
        print(f"Amount Due: {coke_price}")
        coin = int(input("Insert Coin: "))
        match coin:
            case 25:
                coke_price -= 25
            case 10:
                coke_price -= 10
            case 5:
                coke_price -= 5
        if coke_price == 0:
            print(f"Change Owed: {coke_price}")
            break


main()
