class bank:
    def __init__(self):
        self.accounts = []
    def create_account(self):
        account_number = input("Enter account number: ")
        for account in self.accounts:
            if account[0] == account_number:
                print("Account number already exists.")
                return
        name = input("enter name of account holder:")
        password = input("enter password:")
        balance = float(input("enter balance:"))
        self.accounts.append([account_number,name,balance,password])
        print(f"account created successfully {name}.")
    def deposit(self):
        account_number = input("Enter account number: ")
        password = input("Enter password: ")
        for account in self.accounts:
            if account[0] == account_number and account[3] == password:
                amount = float(input("Enter amount to deposit:"))
                if amount > 0:
                    account[2] += amount
                    print(f"Amount deposited successfully.")
                else:
                    print("Amount should be positive.")
                return
        print("Account not found. Please create your account.")

    def withdraw(self):
        account_number = input("Enter account number: ")
        password = input("Enter password: ")
        for account in self.accounts:
            if account[0] == account_number and account[3] == password:
                amount = float(input("Enter amount to withdraw: "))
                if 0 < amount < account[2]:
                    account[2] -= amount
                    print("Withdrawal successful.")
                else:
                    print("Insufficient balance.")
                return
        print("Account not found. Please create your account.")
    def getbalance(self):
        account_number = input("accounr number")
        password = input("enter password")
        for account in self.accounts:
            if account[0] == account_number and account[3] == password:
                print(f"account balance:{account[2]}")
                return
        print("Account not Found, Please Create Your Account")
    def exit(self):
        print("exiting")
        print("....")
        exit()
def main():
    b = bank()
    while True:
        print("1. Create New Account")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Get Account Balance")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            b.create_account()
        elif choice == 2:
            b.deposit()
        elif choice == 3:
            b.withdraw()
        elif choice == 4:
            b.getbalance()
        elif choice == 5:
            b.exit()
        else:
            print("Enter a valid choice.")
if __name__ == "__main__":
    main()






