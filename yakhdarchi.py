# یخدارچی
# https://quera.org/problemset/3429

samovar_temperature = int(input())

if samovar_temperature > 100:
    print("Steam")
elif samovar_temperature < 0:
    print("Ice")
else:
    print("Water")