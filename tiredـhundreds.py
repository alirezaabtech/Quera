# صدگان خسته
# https://quera.org/problemset/3406

first_number = input()
second_number = input()

rfirst_number = int(first_number[::-1])
rsecond_number = int(second_number[::-1])

if rfirst_number == rsecond_number:
    print(first_number,"=",second_number)
elif rfirst_number < rsecond_number:
    print(first_number, "<",second_number)
else:
    print(second_number, "<",first_number)