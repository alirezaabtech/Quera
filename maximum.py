# ماکزیمم
# https://quera.org/problemset/588

def max(list_of_numbers):
    max_number = int(list_of_numbers[0])
    for i in list_of_numbers[1:]:
        if int(i) > max_number:
            max_number = int(i)
    return max_number

count_of_numbers = int(input())
list_of_numbers = input().split(" ")
# max_number = int(list_of_numbers[0])
# for i in range(count_of_numbers):
#     if int(list_of_numbers[i]) > max_number:
#         max_number = int(list_of_numbers[i])
    
# print(max_number)
print(max(list_of_numbers))