# stop watch
import time

my_time = int(input('Please give a time:'))

for x in range (my_time,0,-1):
    second = x % 60
    minutes = x // 60 % 60
    print(f'{minutes:02}:{second:02}')
    time.sleep(1)
print('Time up!')
