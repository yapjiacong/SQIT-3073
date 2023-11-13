# Boolean
for_sale = True
if for_sale:
    print('The product is sales.')
else:
    print('The product is not yet sales.')    

# If else

age = int(input('Please write your age:'))
if age >= 18:
    print('You can register.')
else:
    print('Your are not eligible to register.')

# elif => else if 
age = int(input('Please write your age:'))
if age >= 100:
    print('Your age too high, not eligible register.')
elif age >= 18:
    print('You are eligible.')
elif age<0:
    print('You are not yet born.')
else:
    print('You must 18 years old.')    

    

 