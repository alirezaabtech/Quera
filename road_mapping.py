# جاده کشی
# https://quera.org/problemset/2637

number_of_roads = int(input())
half_roads_1 = number_of_roads // 2
half_roads_2 = number_of_roads - half_roads_1
half_roads_1 += 1
half_roads_2 += 1

print(half_roads_1 * half_roads_2)