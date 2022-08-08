"""
1. class has data (Property) + Functions (Behaviour)
2. class name should be  PascalCase. a. data+methods snake_case

3. data is private

4. for built-in objects like list python uses object-literals to create class
   directly.


5. Methods are functions created inside class. and other difference is way of calling it.

part-1
Creating classes for atm


What is instance variable: values different for diff. object

class objects are mutable
"""
class ATM:
    # static/class  variable are always created outside constructor
    __counter = 1
    def __init__(self):
        """
        __init__ special method also known as constructor/ magic method/ dunder. code inside constructor is automatically
        initiated whenever object of given class is created.

        Use of constructor -- to define variables

        Static variable or class variable
        """
        self.__pin = "" # __ used to make instance variable private
        self.__balance = 0 # Nothing is python is truly private
        """
        using '__' variable is treated as _ClassName.__variableName as instance name 
        """
        ATM.__counter = ATM.__counter + 1
        self.menu()

    @staticmethod
    def get_counter():
        return ATM.__counter

    @staticmethod
    def set_counter(new_counter):
        if type(new_counter) == int:
            ATM.__counter = new_counter
        else:
            print('invalid counter')



    def menu(self):
        user_input = input(""" Hello. How would you like to proceed? \n 
        1. Enter 1 to create pin \n
        2. Enter 2 to deposit \n
        3. Enter 3 to withdraw \n
        4. Enter 4 to check balance \n
        5. Enter 5 to exit
        """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print('Bye')

    def create_pin(self):
        self.__pin = input("Enter your pin")
        print("PIN set successfully")

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self._pin:
            amount = int(input("Enter the amount"))
            self.__balance = self.__balance+amount
            print("deposit successful")
        else:
            print("Enter Valid pin")

    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("Withdrawal Complete!")
            else:
                print("Insufficient Funds")
        else:
            print("invalid pin")

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            print(self.__pin)
        else:
            print("Enter Valid pin")








"""
part-2 
Creating instance of class
"""

sbi = ATM()