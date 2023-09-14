# class_objrcts_for_atm
class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""Hello, how would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
""")
        if user_input == '1':
            self.create_pin() 
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':  # Fixed: Added a colon at the end of this line
            self.withdraw()
        elif user_input == '4':  # Fixed: Added a colon at the end of this line
            self.check_balance()
        else:
            print("bye")

    def create_pin(self):
        self.pin = input("Enter Your pin")  # Fixed: Typo "slef" should be "self"

    def deposit(self):
        temp = input("Enter Your pin")
        if temp == self.pin:  # Fixed: Typo "self.pn" should be "self.pin"
            amount = int(input("Enter the amount"))
            self.balance = self.balance + amount
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = input("Enter Your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            if amount <= self.balance:  # Fixed: Changed "<" to "<="
                self.balance = self.balance - amount
                print("Operation successful")
            else:
                print("Insufficient amount")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter Your pin")  # Fixed: Typo "int("Enter Your pin")" should be "input("Enter Your pin")"
        if temp == self.pin:
            print("Your balance", self.balance)
        else:
            print("Invalid pin")

# Create an instance of the Atm class to start the ATM application
atm = Atm()
