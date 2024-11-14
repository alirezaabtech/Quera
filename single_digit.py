# تک‌رقمی
# https://quera.org/problemset/3539

number = int(input())
temp = int()

while number >= 10:
    total = 0
    for _ in range(len(str(number))):
        temp = number % 10
        total += temp
        number //= 10 
    
    number = total
    
print(number)
