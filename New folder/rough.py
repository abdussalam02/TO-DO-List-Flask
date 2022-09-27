import time

class Account:

    def __init__(self):
        self.name = "Abdussalam"
        self.bal = 9500

    def deposit(self, add):
        self.bal += add
        print("Current balance >> ", self.bal)

    def withdraw(self, remove):
        self.bal -= remove
        print("Current balance >> ", self.bal)

    def display(self):
        print("Account balance for", self.name, "is", self.bal)
        
acc = Account()

print("Hello, Mr.", acc.name)
print("Welcome to Anonymous Bank")
print("")
print("1.) Deposit Money                2.) Withdraw Money")
print("3.) Check Balance                4.) Exit")
print("")

while True:
    option = int(input("Choose any of the option above >> "))

    if option == 1:
        a = int(input("Enter the amount you want to deposit >> "))
        print("Collecting...")
        time.sleep(2)
        acc.deposit(a)
    elif option == 2:
        b = int(input("Enter the amount you want to withdraw >> "))
        print("Withdrawing...")
        time.sleep(2)
        acc.withdraw(b)
    elif option == 3:
        acc.display()
    elif option == 4:
        print("Exited Successfully")
        break
    else:
        print("Choose correct option")
        print("It was a pleasure doing banking with you")
        continue
