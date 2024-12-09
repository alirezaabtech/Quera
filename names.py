# اسم‌ها
# https://quera.org/problemset/2529

number_of_names = int(input())
number_of_letter = []
for _ in range(number_of_names):
    names = input()
    letters = set(names)
    # for i in names:
    #     letters.add(i)
    number_of_letter.append(len(letters))
print(max(number_of_letter))
