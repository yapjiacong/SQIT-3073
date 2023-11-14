# temperature conversion

unit = input('Please insert temperature unit(C,F):').upper()
temp = float(input('Please insert your temperature:'))

if unit == 'C':
    temp = round(9*temp/5+32)
    print(f'Your current temperature is{temp} F')
elif unit == 'F':
    temp = round((temp -32)*5/9)
    print(f'Your current temperature is {temp} C')
else:
    print('Unkown unit!!')
