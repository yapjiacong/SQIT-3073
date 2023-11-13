# Calculator

operator = input('Please insert an operator(add:+, subtract:- , multiple: * , divide: /)')
num1 = float(input('Please insert a number:'))
num2 = float(input('Please insert another number:'))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2    
elif operator == '*':
    result = num1 * num2    
elif operator == '/':
    result = num1 / num2  
else:
    print('Unkown symbol!')

print(f'Your result is{result}')
