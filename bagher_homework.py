# مشق امشب باقر
# https://quera.org/problemset/10230?tab=description

angle_1, angle_2, angle_3 = input().split(" ")
angle_1 = int(angle_1)
angle_2 = int(angle_2)
angle_3 = int(angle_3)

if angle_1 and angle_2 and angle_3 > 0:
    if angle_1 + angle_2 + angle_3 == 180:
        print("Yes")
    else:
        print("No")
else:
    print("No")

# a , b, c =input().split(" ")
# a = int(a)
# b = int(b)
# c = int(c)

# if a == 0 or b == 0 or c == 0:
#     print("No")

# elif a + b + c == 180:
#     print("Yes")

# else:
#     print("No")