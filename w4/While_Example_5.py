# Number

num = int(input('Please state one of the number between 1 to 10 : '))
while num<1 or num>10:
    print(f'Your number is {num} is unvalid.')
    num = int(input('Please choose one number between 1 to 10:'))
print(f'Your number is {num}.')


