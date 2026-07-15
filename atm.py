class Atm:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
    
    def menu(self):
                while True:
                    user_input=input("""
                                     Hello how you like to proceed?
                                     1.Press 1 for Create ATM PIN.
                                     2.Press 2 for Deposit money.
                                     3.Press 3 for withdraw.
                                     4.press 4 to check the balance .
                                     5.press 5 to exit.
""")
                    if user_input=="1":
                         self.Create_PIN()
                    elif user_input=="2":
                         self.deposit()
                    elif user_input=="3":
                         self.withdraw()
                    elif user_input=="4":
                         self.check_balance()
                    elif(user_input=="5"):
                         print("Thank You and have a nice day")
                         break
                    else:
                         print("Invalid input")

    def Create_PIN(self):
        self.pin=int(input("Enter the PIN: "))
        print("Your PIN set succesfully")
    def deposit(self):
        temp=int(input("Enter your pin:"))
        if(temp==self.pin):
            amount=int(input("Enter the amount"))
            self.balance=self.balance+amount
            print("Your amount is successfully Credited.")
        else:
            print("You enter the wrong PIN")
    def withdraw(self):
        temp=int(input("Enter your pin:"))
        if(temp==self.pin):
            amount=int(input("Enter the amount"))
            if(amount<self.balance):
                self.balance=self.balance-amount
                print("The amount is successfully debited.")
            else:
                print("Insuffient Balance you have")
        else:
            print("Your enter the Wrong PIN")

    def check_balance(self):
        temp=int(input("Enter your pin:"))
        if(temp==self.pin):
            print("Your Current Balance is ",self.balance)
        else:
            print("You Enter Wrong PIN")

obj=Atm()





        


    

        
