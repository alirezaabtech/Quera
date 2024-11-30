# اعداد اول
# https://quera.org/problemset/293

import math

start_number = int(input())
end_number = int(input())

if start_number < 2:
    start_number = 2

for i in range(start_number , end_number+1):
    check_number = 1
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            check_number = 0
            break
    if check_number == 1:
        print(i)