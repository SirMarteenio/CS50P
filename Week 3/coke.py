def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        human = input("Insert Coin: ").strip()
        if check(human) is True:
            amount_due = amount_due - int(human)

    change_owed = int(amount_due / -1)
    if amount_due == 0:
        print("Change Owed: 0")
    else:
        print(f"Change Owed: {change_owed}")


def check(a):
    coins = ["25", "10", "5"]
    if a in coins:
        return True
    else:
        return False

main()
