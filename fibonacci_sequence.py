# رشته فیبوناچی
# https://quera.org/problemset/17675

def fib(x):
    a , b = 1 , 2
    fibo_list = [1, 2]
    i = 0
    while i < x-1:
        i = a + b
        fibo_list.append(i)
        a = b
        b = i
    return fibo_list

number = int(input())
fibonacci_numbers = fib(number)

for i in range(1,number+1):
    if i in fibonacci_numbers:
        print("+",end = "")
    else:
        print("-",end = "")