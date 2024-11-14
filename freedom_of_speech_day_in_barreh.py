# روز آزادی بیان در برره
# https://quera.org/problemset/10162?tab=description

number_of_insults =int(input())
first_to_be_angry = 1
i = 1
while True:
    if number_of_insults < i:
        break
    first_to_be_angry += 1
    i += 1

if first_to_be_angry % 2 == 0:
    print("Payin Barare")
else:
    print("Bala Barare")

# n = int(input())

# if n %2 == 0:
#     print("Bala Barare")
    
# else:
#     print("Payin Barare")