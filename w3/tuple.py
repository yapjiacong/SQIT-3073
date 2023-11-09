import os
os.system('cls')

a = []
print(a)

buah = ('durian','manggis','rambutan')
#print(buah[-1])

#a = (1,2,'a','g',98)
#print(a[2:4])

#for i in buah:
   # print(i)

buahbuahan = ('pisang',)
buah+= buahbuahan
print(buah)

buahbuahan=list(buah)
print(buah)
buahbuahan.remove('pisang')
buah = tuple(buahbuahan)
print(buah)


