for y in range(5):
    for x in range(1,10):
        print(x,end=' ')
    print()


row = int(input('Please insert a row:'))
cols = int(input('Please insert a column:'))
symbol = input('Please insert a symbol:')

for i in range(row):
    for j in range(cols):
        print(symbol, end=' ')
    print()     