
class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.Name = full_name
        self.AccountNumber = account_number
        self.Route = routing_number
        self.Balance = balance

    def deposit(self, amount):
        self.Balance = amount + self.Balance
        print(f"Amount Deposited: ${amount}")

    def widthdrawl(self, amount):
        if amount > self.Balance:
            self.Balance = self.Balance - amount
            print("Insufficient Funds")
            self.Balance = self.Balance - 10 
            print(f'Amount Withdrawn ${amount}')
        else:
            self.Balance = self.Balance - amount
            print(f'Amount Withdrawn ${amount}')

    def get_balance(self):
        print(f'{self.Name}. Your account balance is ${round(self.Balance,2)} ')

    def add_interest(self):
        interest = self.Balance * 0.00083
        self.Balance = self.Balance + interest
    
    def print_receipt(self):
        encrypt = "****"
        print(self.Name)
        print(f'Account No.: {encrypt + self.AccountNumber[4:9]}')
        print (f'Routing No.: {self.Route}')
        print(f'Balance: ${round(self.Balance,2)}')


        # 3 Personal Accounts 
SamuelMadrigal = BankAccount('Samuel Madrigal','87654321', 12345678, 50.00)
RafaVasquez = BankAccount('Rafa Vasquez', '12345678', 87654321, 60.00)
AlexTurcanu = BankAccount('Alex Turcanu', '17473895', 14367489, 70.00)


print('Welcome!')

SamuelMadrigal.add_interest()
SamuelMadrigal.widthdrawl(13.00)
SamuelMadrigal.get_balance()

RafaVasquez.add_interest()
RafaVasquez.deposit(27.00)
RafaVasquez.get_balance()

AlexTurcanu.widthdrawl(15.00)
AlexTurcanu.add_interest()
AlexTurcanu.get_balance()

SamuelMadrigal.print_receipt()
RafaVasquez.print_receipt()
AlexTurcanu.print_receipt()