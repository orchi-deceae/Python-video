
class BalanceException(Exception): 
    pass


##########################################################

class BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def dispBalc_(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def errHandle_(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f'\nSorry, account \'{self.name}\' only has a balance of ${self.balance}')
        
    def deposit(self, amount):
        self.balance = self.balance + amount

        print(f"\nDeposite complete.",end='')
        self.dispBalc_()

    def withdraw(self, amount):
        try:
            self.errHandle_(amount)
            self.balance = self.balance - amount

            print('\nWithdrew complete',end='')
            self.dispBalc_()
            
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, other_acc):
        try:
            print('\n\n**********\nBeginning Transfer..🚀')
            self.errHandle_(amount)
            self.withdraw(amount)
            other_acc.deposit(amount)

            print('\nTransfer complete! check✅\n\n**********\n')
        
        except BalanceException as error:
            print(f'\nTransfer interupted. ❌ {error}')


##########################################################

class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        # return super().deposit(amount)
        self.balance = self.balance + (amount * 1.05)

        print('\nDeposit complete.',end='')
        self.dispBalc_()


##########################################################

class savingAccount(InterestRewardAcct):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount):
        # return super().withdraw(amount)
        try:
            self.errHandle_(amount + self.fee)
            self.balance = self.balance - (amount - self.fee)

            print('\nWithdrew complete',end='')
            self.dispBalc_()
            
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
    
        