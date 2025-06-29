from bank_account import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.dispBalc_()
Sara.dispBalc_()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(10000, Sara)
Dave.transfer(100, Sara)

Jim = InterestRewardAcct(1000, 'Jim')

Jim.dispBalc_()

Jim.deposit(100)

Jim.transfer(100, Dave)

Blaze = savingAccount(1000, 'Blaze')

Blaze.dispBalc_()

Blaze.deposit(100)

Blaze.transfer(1000, Sara)
