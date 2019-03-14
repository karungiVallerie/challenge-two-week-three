class BankAccount:

    def __init__(self, name,account_number, balance=0.00):
        self.account_number = account_number
        self.name = name
        self._balance = balance

    def deposit(self, amount):
        """make a deposit""" 
        self._balance = self._balance  + amount
        return self._balance

    def withdraw(self, amount):
        """make a withdraw"""
        if amount > self._balance:
                raise ValueError("insufficient funds")
        self._balance = self._balance - amount
        return self._balance      

    def get_balance(self):
        return self._balance

# account1 = BankAccount('vallerie',123425678)#here we pass all the parameters apart from the balance because (it has a value) above in the  function(def)
# a n     ccount1.deposit(2000000)
# account1.withdraw(3400)    