# خر در چمن فراوونه!!
# https://quera.org/problemset/4065

rhithm_a, rhithm_b, number_of_times = input().split(" ")
time_of_last_bray = 0

for i in range(int(number_of_times)):
    if i % 2 == 0:
        time_of_last_bray += int(rhithm_a)
    else:
        time_of_last_bray += int(rhithm_b)
print(time_of_last_bray)