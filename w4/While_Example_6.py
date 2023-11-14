# compound interest calculator

amount = 0
rate = 0
time = 0 

while amount <= 0:
    amount = float(input('Please state your amount:'))
    if amount <= 0:
      print('Amount cannot be 0 or less than 0.')


while rate <=0:
    rate = float(input('Please insert your rate:'))
    if rate <= 0:
        print('Rate cannot be 0 or less than 0.')


while time <=0:
    time = int(input('Please give a year: '))
    if time <= 0:
        print('Time cannot be 0 or less than 0.')

print('Amount: ',amount )
print('Rate: ',rate )
print('Time: ' , time )

total = amount *(1+(rate/100))**time
print('Total amount: ',total)