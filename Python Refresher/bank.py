# Creat a bank class that initialize with swift code, bank name, branch namee, branch location.
class Bank:
    def __init__(self, swift_code='0000', bank_name='First', branch_name='New York Branch', loc='New York'):
        self.swift_code = swift_code
        self.bank_name = bank_name
        self.branch_name = branch_name
        self.loc = loc

    def __repr__(self):
        return (" Welcome to {b} Bank.\
        \n Swift code: {sw}\n Bank name: {bank}\n Branch name: {branch}\
        \n Bank location: {loc}\n".format(b=self.bank_name, sw=self.swift_code,
                                          bank=self.bank_name,
                                          branch=self.branch_name,
                                          loc=self.loc))


# Create Customer class that has customer name, address and contact details.
class Customer():

    def __init__(self, cust_id, custname, address, contactdetails):
        self.cust_id = cust_id
        self.custname = custname
        self.address = address
        self.contactdetails = contactdetails

    def __repr__(self):
        return ("Customer ID: {cust_id}\n Customer name:{cust_name}\
        \n Customer address:{cust_address}\n Contact Details: {cust_details}\n"
                .format(cust_id=self.cust_id,
                        cust_name=self.custname,
                        cust_address=self.address,
                        cust_details=self.contactdetails))


class Account(Bank):
    ''' Initialize the account information with account id,
    customer object ,and the inital account balance.'''

    def __init__(self, AccountID, cust, opening_balance=0):
        super().__init__()
        self.AccountID = AccountID
        self.balance = opening_balance
        self.cust = cust
    # String representation of account information

    def getAccountInfo(self):
        print("Account# {account_id}, Customer# {cust_id}\
                 \nCustomer {cust_name} has a current balance of ${cust_bal}\
                 \nin {bank_name} bank."
              .format(account_id=self.AccountID,
                      cust_id=self.cust.cust_id,
                      cust_name=self.cust.custname, cust_bal=self.balance,
                      bank_name=self.bank_name))

    # If the customer tries to deposit second banks' chcek return instruciton.
    # Otherwise, increase the account balance
    def deposit(self, amount, tf):
        if (tf.title()) == 'False' or (tf.title()) != 'true':
            print("We cannot accept Second bank's check(s) on this machine.\
                   \nPlease use our mobile service")
        else:
            self.balance = self.balance + amount
        return "You have deposited ${deposit}. Your balance after the deposit is ${bal}".\
            format(deposit=amount, bal=self.balance)

    # Withdraw amount that is less than the balance
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            return ("If you withdraw the amount, your balance will be negative.\
            \n You can only withdraw up to the current balance of ${bal}")\
                .format(bal=self.balance)
        return "After ${withdraw} withdraw, your current balance on this account will be ${bal}"\
            .format(withdraw=amount, bal=self.balance)

# Get current balance of the account
    def getBalance(self):
        return "Your current balance on this account is {bal}".\
            format(bal=self.balance)


class SavingsAccount(Account):
    ''' Initialize the savings account information with account id,
    customer object, and the inital account opening balance.'''

    def __init__(self, saccountid, cust, opening_balance, min_balance):
        print("\n*************************************\
        \n   Opening a new Savings Account\
        \n**************************************\
        \n")

        # Intialize the attributes with parent attributes
        super().__init__(cust, opening_balance)
        self.SAccountID = saccountid
        self.SMinBalance = min_balance
        # Notify the customer about the financial charges
        # when minimum opening balance has not met.
        if self.SMinBalance < 1000:
            print("Your savings has not been met the minimum opening balance of $1000. \
            \nYou will be charged financial fee of **$15/month**. \n")
