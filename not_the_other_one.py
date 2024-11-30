# آخ جون طرف نیست!
# https://quera.org/problemset/3538

week_days = ["shanbe","1shanbe", "2shanbe", "3shanbe", "4shanbe", "5shanbe", "jome"]

for _ in range(3):
    attendance_count = int(input())                     #There's no need to write this part
    attendance_days = input().split(" ")
    for i in attendance_days:
        if i in week_days:
            week_days.remove(i)

print(len(week_days))