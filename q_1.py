''' Question Number # 1::  A banking application allows users to withdraw money. The function withdraw(balance, 
amount) should check if the withdrawal amount is greater than the balance. If yes, it should 
raise an exception "Insufficient funds", otherwise return the new balance. '''

def withdraw(balance, amount):
    if amount > balance:
      raise Exception("Insufficient funds")
    else:
      balance = balance-amount
      return  balance

withdraw(250000,70000)

