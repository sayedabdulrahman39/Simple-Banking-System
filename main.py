def show_balance(balance):
    print("****************balance****************")
    input(f"your balance is: ${balance:2f}")
    print("****************balance****************")

def deposit():
    print("****************deposit****************")
    amount = float(input("enter your deposit amount:"))
    print("****************deposit****************")

    if amount < 0:
        print("this amount cant be deposit")
        return 0
    else:
        return amount

def withdraw(balance):
    print("****************withdraw****************")
    amount = float(input("enter your withdraw amount:"))
    print("****************withdraw****************")

    if amount > balance:
        print("insuffient balance")
        return 0
    elif amount < 0:
        print("the amount should be grether than 0")
        return 0
    else:
        return  amount
    
def main():
    balance = 0
    is_running = True

    while is_running:
        print("---------welcome------------")
        print(     "banking program"        )
        print(      "1.show balance"        )
        print(      "2.deposit"             )
        print(      "3.withdraw"            )
        print(      "4.exit"                )
        print("----------------------------")

        count = input("enter your choice (1-4):")

        if count == '1':
            show_balance(balance)
        elif count == '2':
            balance += deposit()
        elif count == '3':
            balance -= withdraw(balance)
        elif count == '4':
            is_running = False
        else:
             print("enter vaild choice")

    print("---------------------------------------")
    print(   "thank you and have a nice day"  )
    print("---------------------------------------")

if __name__== "__main__":
 main()