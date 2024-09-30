from bank import Bank
import random

class User:
    def __init__(self, name, email, address, account_Type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_Type = account_Type
        self.balance = 0
        self.account_number = str(random.randint(40000, 99999))
        self.transaction_history_list = []
        self.loan_count = int(0)
    
    def Deposit_Money(self, amount, bank: Bank):
        amount = float(amount)
        if amount <= 0:
            print("Please Choose Higher Amount\n")
            return

        self.balance += amount
        bank.bank_balance += amount
        self.transaction_history_list.append(f'Deposited: {amount}')
        print(f"Deposited {amount} TAKA successfully.\n")

    def Withdraw_Money(self, amount,bank: Bank):
        amount = float(amount)
        if amount <= 0:
            print("Please Choose Higher Amount.\n")
            return
        
        if amount > self.balance:
            print("Insufficient balance.\n")
            return
        
        if amount > bank.bank_balance:
            print("The bank is bankrupt.\n")
            return
        
        self.balance -= amount
        bank.bank_balance -= amount
        self.transaction_history_list.append(f"Withdrew: {amount}")
        print(f"Withdrawn {amount}taka successfully!!\n")
    
    
    
    def Check_Balance(self):
        print(f'Available balance = {self.balance}taka\n')

    
    def Transaction_History(self):
        if not self.transaction_history_list:
            print("No Transaction History Available.\n")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history_list:
                print(transaction)

    def Take_Loan(self, amount,bank: Bank):
        amount = float(amount)
        if self.loan_count >= 2:
            print(" No more loans can be taken.\n")
            return

        if bank.loan_feature:
            if  bank.bank_balance >= amount:
                self.balance += amount
                bank.bank_balance -= amount
                self.loan_count += 1
                bank.loan_amount += amount
                print(f"Loan of {amount} TAKA taken successfully.\n\n")
            else:
                print(f"You cannot take a loan more than {bank.bank_balance} TAKA.\n\n")
        else:
            print("Loan feature is currently not available.\n\n")

    def Transfer_Money(self, receiver_account, amount):
        amount = float(amount)
        if amount <= 0:
            print("Please Enter Higher Amount\n")
            return

        if amount > self.balance:
            print("Insufficient balance\n")
            return

        self.balance -= amount
        receiver_account.balance += amount
        self.transaction_history_list.append(f"Transferred: {amount}taka to account {receiver_account.account_number}")
        print(f"Transfer of {amount}taka to account {receiver_account.account_number} successful.\n\n")
