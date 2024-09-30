from user import User
from bank import Bank

class Admin:
    def __init__(self, name, pin, bank: Bank) -> None:
        self.bank = bank
        self.name = name
        self.pin = pin

    def Create_account(self, name, email, address, account_Type, bank: Bank):
        new_user = User(name, email, address, account_Type)
        bank.account_list.append(new_user)
        print(f'\nYour Account number is: {new_user.account_number} ---- Please Remember ----)\n')

    def Delete_account(self, account_number, bank: Bank):
        for account in bank.account_list:
            if account_number == account.account_number:
                bank.account_list.remove(account)
                print(f'\nAccount {account_number} Deleted Successfully!!!\n')
                return
        print(f'\nAccount {account_number} not found\n')

    def See_Account_list(self, bank: Bank):
        print('\nShowing all account list :\n')
        for account in bank.account_list:
            print(f'Name: {account.name}\tAccount Number: {account.account_number}\tAccount Type: {account.account_Type}')

    def Bank_Balance(self, bank: Bank):
        print(f'Total Account Balence = {bank.bank_balance}taka\n')

    def Loan_Amount(self, bank: Bank):
        print(f'Total Loan Account = {bank.loan_amount}taka\n')

    
    
    def Loan_feature(self, on_off: bool,bank: Bank):
        bank.Loan_feature = on_off
        status = "Enabled" if on_off else "Disabled"
        print(f"Loan feature has been {status}\n\n")