# تیم کشی
# https://quera.org/problemset/80651

has_laptop_city_1= int(input())
has_no_laptop_city_1= int(input())
has_laptop_city_2= int(input())
has_no_laptop_city_2= int(input())
has_laptop_city_3= int(input())
has_no_laptop_city_3= int(input())
specificationـlist = [has_laptop_city_1, has_no_laptop_city_1, has_laptop_city_2, has_no_laptop_city_2, has_laptop_city_3 ,has_no_laptop_city_3]
# specificationـlist = []
# for _ in range(6):
#     specificationـlist.append(int(input()))
i = 0
total_max_teams = 0

while i < 6:
    if specificationـlist[i] < specificationـlist[i+1]:
        total_max_teams += specificationـlist[i]
    else:
        total_max_teams += specificationـlist[i+1]
    i += 2

print(total_max_teams)

######### OR #########


# sum = 0
# for i in range(3):
#     a = int(input())
#     b = int(input())
#     if a > b:
#         a , b = b , a
#     sum = sum + a

# print(sum)