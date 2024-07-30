class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self):
        account_number = input("Enter account number: ")
        if account_number in self.accounts:
            print("Account number already exists.")
            return
        name = input("Enter name of account holder: ")
        password = input("Enter password: ")
        try:
            balance = float(input("Enter balance: "))
            if balance < 0:
                print("Balance cannot be negative.")
                return
        except ValueError:
            print("Invalid balance input.")
            return
        self.accounts[account_number] = {'name': name, 'balance': balance, 'password': password}
        print(f"Account created successfully for {name}.")
    
    def deposit(self):
        account_number = input("Enter account number: ")
        password = input("Enter password: ")
        account = self.accounts.get(account_number)
        if account and account['password'] == password:
            try:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    account['balance'] += amount
                    print("Amount deposited successfully.")
                else:
                    print("Amount should be positive.")
            except ValueError:
                print("Invalid deposit amount.")
        else:
            print("Account not found or incorrect password.")
    
    def withdraw(self):
        account_number = input("Enter account number: ")
        password = input("Enter password: ")
        account = self.accounts.get(account_number)
        if account and account['password'] == password:
            try:
                amount = float(input("Enter amount to withdraw: "))
                if 0 < amount <= account['balance']:
                    account['balance'] -= amount
                    print("Withdrawal successful.")
                else:
                    print("Insufficient balance or invalid amount.")
            except ValueError:
                print("Invalid withdrawal amount.")
        else:
            print("Account not found or incorrect password.")
    
    def get_balance(self):
        account_number = input("Enter account number: ")
        password = input("Enter password: ")
        account = self.accounts.get(account_number)
        if account and account['password'] == password:
            print(f"Account balance: {account['balance']}")
        else:
            print("Account not found or incorrect password.")
    
    def exit_program(self):
        print("Exiting the program...")
        exit()

def main():
    bank = Bank()
    while True:
        print("\n1. Create New Account")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. Get Account Balance")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                bank.create_account()
            elif choice == 2:
                bank.deposit()
            elif choice == 3:
                bank.withdraw()
            elif choice == 4:
                bank.get_balance()
            elif choice == 5:
                bank.exit_program()
            else:
                print("Enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
