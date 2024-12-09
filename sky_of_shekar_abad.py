# آسمان شکر آباد
# https://quera.org/problemset/6082

row , column = input().split(" ")
row = int(row)
number_of_stars = 0
for _ in range(row):
    celestial_bodies = input()
    for i in celestial_bodies:
        if i == "*":
            number_of_stars += 1

print(number_of_stars)