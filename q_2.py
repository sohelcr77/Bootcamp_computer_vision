''' Question Number # 2::  You are building a calculator app. Write a Python function calculate() that takes two 
numbers and an operator (+, -, *, /) as input and returns the result. '''

def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
        
    elif operator == '-':
        return number1 - number2

    elif operator == '*':
        return number1 * number2

    elif  operator == '/':
        return number1 / number2  
        
    else:
        return "Invalid operation"
   
   
print(calculate(100,20,'+'))
print(calculate(100,20,'-'))
print(calculate(100,20,'*'))
print(calculate(100,20,'/'))

