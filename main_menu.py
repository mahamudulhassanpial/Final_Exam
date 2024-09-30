from bank import Bank
from admin import Admin
from user import User

def Main_Menu():
    print(f"\n------------Welcome to {Digital_Bank.name}---------\n")
    print("Please Log in as:\n1. User\n2. Admin\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        User_menu()
    elif choice == '2':
        Admin_Menu()

    elif choice == '3':
        print("Exiting...")
    else:
        print("Invalid choice.\n\n")
        Main_Menu()


# For the user
def User_menu():
    if not Digital_Bank.account_list:
        print("Create An User Account First. Select Admin Menu\n\n")
        Main_Menu()
    else:
        print("1. Deposit_Money")
        print("2. Withdraw_Money")
        print("3. Check Balance")
        print("4. Transfer Money")
        print("5. Transaction History")
        print("6. Take Loan")
        print("7. Log Out")
    
        choice = input("Enter your choice: ")

        if choice == '1':
            Deposit_Money()
        elif choice == '2':
            Withdraw_Money()
        elif choice == '3':
            Check_Balance()
        elif choice == '4':
            Transfer_Money()
        elif choice == '5':
            Transaction_History()
        elif choice == '6':
            Take_Loan()
        elif choice == '7':
            Main_Menu()
        else:
            print("Invalid choice.\n\n")
            User_menu()




# For the admin
admin_authenticated = False

def Admin_Menu():
    global admin_authenticated
    if not Digital_Bank.admin_list:
        print("Be An Admin First.\n\n")
        print('Create Admin Account: 1.YES  2.NO')
        disition = input("Enter the option: ")
        if disition == '1':
            A_name = input("Enter Name: ")
            Pin = input("Enter Password: ")
            global my_admin
            my_admin = Admin(A_name, Pin, Digital_Bank)
            Digital_Bank.admin_list.append(my_admin)
            print("Admin Created Successfully!!!\n")
            admin_authenticated = True
            Admin_Menu()
        else:
            print("Exiting to Main Menu.....\n")
            Main_Menu()
    else:
        if not admin_authenticated:
            code = input("Enter Pin to Access the Account: ")
            for admin in Digital_Bank.admin_list:
                if code == admin.pin:
                    print("Admin Menu:")
                    admin_authenticated = True
                    break
            else:
                print("Wrong pin number\nEnter the wright pin number")
                Admin_Menu()

        print("Admin Menu:")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. See Account List")
        print("4. Bank Balance")
        print("5. Loan Amount")
        print("6. Loan Feature Control")
        print("7. Log Out")

        choice = input("Enter your choice: ")
        if choice == '1':
            Admin_Create_Account()
        elif choice == '2':
            Admin_Delete_Account()
        elif choice == '3':
            Admin_See_Account_List()
        elif choice == '4':
            Admin_Bank_Balance()
        elif choice == '5':
            Admin_Loan_Amount()
        elif choice == '6':
            Admin_Loan_Feature()
        elif choice == '7':
            admin_authenticated = False
            Main_Menu()
        else:
            print("Invalid Choice.\n")
            Admin_Menu()


def Deposit_Money():
    account_number = input("Enter your account number: ")
    amount = float(input("Enter Deposit amount: "))
    for acc in Digital_Bank.account_list:
        if account_number == str(acc.account_number):
            acc.Deposit_Money(amount,Digital_Bank)
            break
    else:
        print("Account not found.\n\n")
    User_menu()


def Withdraw_Money():
    account_number = input("Enter Your Account Number: ")
    amount = float(input("Enter Withdraw Amount: "))
    for acc in Digital_Bank.account_list:
        if account_number == acc.account_number:
            acc.Withdraw_Money(amount,Digital_Bank)
            break
    else:
        print("Account not found.\n\n")
    User_menu()

def Check_Balance():
    account_number = input("Enter Your Account Number: ")
    for account in Digital_Bank.account_list:
        if account_number == account.account_number:
            account.Check_Balance()
            break
    else:
        print("Account not found.\n\n")
    User_menu()

def Transfer_Money():
    sender_account_number = input("Enter Your Account Number: ")
    receiver_account_number = input("Enter Receiver's Account Number: ")
    amount = float(input("Enter amount to transfer: "))
    sender_acc = None
    receiver_acc = None
    for account in Digital_Bank.account_list:
        if sender_account_number == account.account_number:
            sender_acc = account
        if receiver_account_number == account.account_number:
            receiver_acc = account
    
    if sender_acc and receiver_acc:
        sender_acc.Transfer_Money(receiver_acc, amount)
    else:
        if not sender_acc:
            print("Sender account not found\n")
        if not receiver_acc:
            print("Receiver account not found\n")
    User_menu()



def Transaction_History():
    account_number = input("Enter your account number: ")
    for account in Digital_Bank.account_list:
        if account_number == account.account_number:
            account.Transaction_History()
            break
    else:
        print("\nAccount does not exist\n")
    User_menu()

def Take_Loan():
    Account_number = input("Enter Your Account Number: ")
    amount = input("Enter Loan Amount: ")
    for account in Digital_Bank.account_list:
        if Account_number == account.account_number:
            account.Take_Loan(amount, Digital_Bank)
            break
    else:
        print('Account does not exist\n')
    User_menu()


def Admin_Create_Account():
    name = input("Enter Account Holder's Name: ")
    email = input("Enter E-mail Address: ")
    address = input("Enter Address: ")
    account_type = input("Enter Account Type (e.g., savings, checking): ")
    my_admin.Create_account(name, email, address, account_type,Digital_Bank)
    Admin_Menu()

def Admin_Delete_Account():
    account_number = input("Enter Account Number to Delete: ")
    my_admin.Delete_account(account_number,Digital_Bank)
    Admin_Menu()

def Admin_See_Account_List():
    my_admin.See_Account_list(Digital_Bank)
    Admin_Menu()

def Admin_Bank_Balance():
    my_admin.Bank_Balance(Digital_Bank)
    Admin_Menu()

def Admin_Loan_Amount():
    my_admin.Loan_Amount(Digital_Bank)
    Admin_Menu()

def Admin_Loan_Feature():
    print('Enable loan feature? (1.Yes  2.No)')
    choice = input("Enter the option: ")
    if choice == '1':
        my_admin.Loan_feature(True, Digital_Bank)
        Admin_Menu()
    elif choice == '2':
        my_admin.Loan_feature(False, Digital_Bank)
        Admin_Menu()


    


Digital_Bank = Bank("SONALI BANK PLC")

Main_Menu()