# اعداد فیثاغورثی
# https://quera.org/problemset/280

a = int(input())
b = int(input())
c = int(input())

a *= a
b *= b
c *= c

if a == b + c:
    print("Yes")
elif b == a + c:
    print("Yes")
elif c == a + b:
    print("Yes")
else:
    print("No")

# sides = {
#     a: [b, c],
#     b: [a, c],
#     c: [a, b]
# }

# is_triangle = 'NO'
# for key, value in sides.items():
#     if key * key == value[0] * value[0] + value[1] * value[1]:
#         is_triangle = 'YES'
#         break

# print(is_triangle)