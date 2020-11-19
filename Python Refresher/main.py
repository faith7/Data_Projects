from bank import Bank, Customer, Account, SavingsAccount

customers = {}
checkings = {}
savings = {}

# Create an instance of a Bank and print out the first screen on the console.
b1 = Bank()
print("Welcome!")
print(b1)


# To show transaction types
def transaction_type_screen():
    print("Please enter transaction type: \n\
            1. Create a new account \n\
            2. Deposit \n\
            3. Withdraw \n\
            4. Balance Inqury \n\
            5. Exit Transaction")


# To show account types
def account_type_screen():
    print("Select the account type: \
                \n 1.checkig\
                \n 2.savings")


# Receive customer related inputs and create instance of customer
# by comparing exisitng customers in the dictionary
def create_customers():
    print("Enter customer_id")
    try:
        cust_id = int(input())
    except:
        print("Please enter an integer number")

    if cust_id in customers:
        print("Customer ID already exists. Cannot be recreated...")
        print(customers[cust_id])
        return customers[cust_id]

    else:
        print("Welcome, new customer!.")
        print("Enter customer_name")
        custname = input()
        print("Enter customer_address")
        address = input()
        print("Enter contact details")
        contactdetails = input()
        c = Customer(cust_id, custname, address, contactdetails)
        customers[cust_id] = c
        return c


# Receive customer related inputs and create instance of customer
# by comparing exisitng customers in the dictionary
def create_checking_account(c):
    print("Enter Checking Account_id")
    try:
        account_id = int(input())
    except ValueError:
        print("Please enter an integer number")

    if c.cust_id in customers and account_id in checkings:
        print("Checking Account ID aleady exists")
        print(checkings[account_id].getAccountInfo())
        return checkings[account_id]
    else:
        print("Type opening balance")
        opening_balance = int(input())
        a1 = Account(account_id, c, opening_balance)
        checkings[account_id] = a1
        return a1


# Receive customer related inputs and create instance of customer
# by comparing exisitng customers in the dictionary
def create_savings_account(c):
    print("Enter Savings Account_id")
    try:
        savings_id = int(input())
    except ValueError:
        print("Please enter an integer number")
    if c.cust_id in customers and savings_id in savings:
        print("Savings Account ID aleady exists")
        print(savings[savings_id].getAccountInfo())
        return savings[savings_id]

    # Or savings id is new, request additonal information
    else:
        print("Type opening balance")
        opening_balance = int(input())
        print("Type min balance")
        min_balance = int(input())
        s1 = SavingsAccount(savings_id, c, opening_balance, min_balance)
        savings[savings_id] = s1
        return s1


# Flag condition to continue the loop
flag = True

# To show transaction types


def transaction_type_screen():
    print("Please enter transaction type: \n\
            1. Create a new account \n\
            2. Deposit \n\
            3. Withdraw \n\
            4. Balance Inqury \n\
            5. Exit Transaction")


# Repeat the
while(flag):
    transaction_type_screen()
    transaction_type = int(input())

    try:
        # Cancel the transaction and revert to the prior screen
        if transaction_type == 5:
            print("Canceling Checking Account Transaction and exit")
            break
        else:
            c = create_customers()
            print("Some input is in wrong format.")
            # If create a new account transaction type is selected
            if transaction_type == 1:
                account_type_screen()
                account_type = int(input())

                if account_type == 1:
                    checking = create_checking_account(c)
                    checking.getAccountInfo()

                if account_type == 2:
                    saving = create_savings_account(c)
                    saving.getAccountInfo()

            # If a deposit function is created
            elif transaction_type == 2:
                account_type_screen()
                account_type = int(input())

                if account_type == 1:
                    checking = create_checking_account(c)
                    print("Enter the deposit amount")
                    deposit = int(input())
                    print("Enter t if it's a second bank's check")
                    cash = input()
                    print(checking.deposit(deposit, cash))

                if account_type == 2:
                    saving = create_savings_account(c)
                    print("Enter the deposit amount")
                    deposit = int(input())
                    print("Enter true if it's cash, otherwise false")
                    cash = input()
                    print(saving.deposit(deposit, cash))

            # If a withdrawl function is created
            elif transaction_type == 3:
                account_type_screen()
                account_type = int(input())

                if account_type == 1:
                    checking = create_checking_account(c)
                    print("Enter the withdrawl amounnt")
                    withdrawl = int(input())
                    print(checking.withdraw(withdrawl))

                if account_type == 2:
                    saving = create_savings_account(c)
                    print("Enter the withdrawl amounnt")
                    withdrawl = int(input())
                    print(saving.withdraw(withdrawl))

            # If balance inqury transaction is selected
            elif transaction_type == 4:
                account_type_screen()
                account_type = int(input())
                if account_type == 1:
                    checking = create_checking_account(c)
                    checking.getBalance()

                if account_type == 2:
                    saving = create_savings_account(c)
                    saving.getBalance()

            else:
                print("Please choose integer number between 1-5")
                continue
    except:
        print("Some formats are wrong. Please enter the right format again.")
