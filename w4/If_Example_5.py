# weight conversion

weight = float(input('Please insert your weight:'))
unit = input('Your weight is kg/lb?').upper()


if unit == 'KG':
    weight *= 2.2
    new_unit = 'lb'
elif unit == 'LB':
    weight /= 2.2
    new_unit = 'KG'
else:
    print('Your unit is incorrect.')
    exit()    
print(f'Your weight is {round(weight)}{new_unit}')