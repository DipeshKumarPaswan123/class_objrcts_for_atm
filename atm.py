Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0

        self.menu()
    def menu(self):
        user_input = input(""" Hello, how would you like to proceed?
        1.Enter 1 to create pin
        2.Enter 2 to deposit
        3.Enter 3 to withdraw
        4. Enter 4 to check balance
        5.Enter 5 to exit
""")
        if user_input == '1':
            self.create_pin() 
        elif user_input == '2':
            self.deposit()
        elif user_input == '3'
            self.withdraw()
        elif user_input == '4'
            self.check_balance()
        else:
            print("bye")
    def create_pin(self):
        slef.pin = input("Enter Your pin")

    def deposit(self):
        temp = input("Enter Your pin")
        if temp == self.pn:
            amount = int(input("Enter the amount"))  
            self.balance = self.balance + amount
        else:
            print("Invalid pin") 

    def withdraw(self):
        temp = input("Enter Your pin")
        if temp == slef.pin:
            amount = int(input("Enter the amount"))
            if amount < self.balance:
                self.balance = self.balance-amount
                print("Operation successfull")
            else:
                print("Insufficient amount")
        else:
            print("Invalid pin")        

    def check_balance(self):
        temp = int("Enter Your pin")
        if temp == self.pin:
            print("Your balance",self.balance)
        else:
            prinnt("Invalid pin")        