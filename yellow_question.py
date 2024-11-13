#سوال زرد
#https://quera.org/problemset/3537?tab=description

amount_of_information = int(input())
amount_of_surprise = "Wo"

while amount_of_information > 1:
    amount_of_surprise +="o"
    amount_of_information -= 1

amount_of_surprise += "W!"
print(amount_of_surprise)