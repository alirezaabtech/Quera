# هندونه‌خوری
# https://quera.org/problemset/35253

number_of_watermelon = int(input())
weight_of_each_watermelon = input().split(" ")
last_watermelon = 0

for i in range(number_of_watermelon):
    if int(weight_of_each_watermelon[i]) > int(weight_of_each_watermelon[last_watermelon]):
        last_watermelon = i

print(last_watermelon + 1)