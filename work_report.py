# گزارش کار
# https://quera.org/problemset/49535

Number_of_bottles, Liquid_volume = input().split(" ")
total_bottles_capacity = 0

for _ in range(int(Number_of_bottles)):
    total_bottles_capacity += int(input())

if total_bottles_capacity >= int(Liquid_volume):
    print("YES")
else:
    print("NO")