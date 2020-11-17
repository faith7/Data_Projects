from bank import Bank, Customer, Account, SavingsAccount


# Create an instance of a Bank
b1 = Bank()


def transaction_type_screen():
    print("Please enter transaction type: \n\
            1. Account Info Inqury \n\
            2. Deposit \n\
            3. Withdraw \n\
            4. Balance Inqury \n\
            5. Exit Transaction")


def account_type_screen():
    print("Select the account type: \
                \n 1.checkig\
                \n 2.savings")


def create_customers():
    print("input customer_id")
    cust_id = int(input())
    print("input customer_name")
    custname = input()
    print("input customer_address")
    address = input()
    print("input contact details")
    contactdetails = input()
    c = Customer(cust_id, custname, address, contactdetails)
    return c


def create_checking_account(c):
    print("Type opening balance")
    opening_balance = int(input())
    a1 = Account(c, opening_balance)
    return a1


def create_savings_account(c):
    print("Type opening balance")
    opening_balance = int(input())
    print("Type min balance")
    min_balance = int(input())
    s1 = SavingsAccount(c, opening_balance, min_balance)
    return s1


# Flag condition to continue the loop
flag = True


while(flag):
    transaction_type_screen()
    transaction_type = int(input())

    # Cancel the transaction and revert to the prior screen
    if transaction_type == 5:
        print("Canceling Checking Account Transaction and exit")
        break
    else:
        c = create_customers()
        if transaction_type == 1:
            account_type_screen()
            account_type = int(input())

            if account_type == 1:
                create_checking_account(c).getAccountInfo()

            if account_type == 2:
                create_savings_account(c).getAccountInfo()

        elif transaction_type == 2:
            account_type_screen()
            account_type = int(input())
            print("Enter the deposit amounnt")
            deposit = int(input())
            print("Enter true if it's cash, otherwise false")
            cash = input()
            if account_type == 1:
                print(create_checking_account(c).deposit(deposit, cash))

            if account_type == 2:
                print(create_savings_account(c).deposit(deposit, cash))

        elif transaction_type == 3:
            account_type_screen()
            account_type = int(input())
            print("Enter the withdrawl amounnt")
            withdrawl = int(input())
            if account_type == 1:
                create_checking_account(c).withdraw(amount)

            if account_type == 2:
                create_savings_account(c).withdraw(amount)

        elif transaction_type == 4:
            account_type_screen()
            account_type = int(input())
            if account_type == 1:
                create_checking_account(c).getBalance()

            if account_type == 2:
                create_savings_account(c).getBalance()

        else:
            print("Please choose integer number between 1-5")
            continue
