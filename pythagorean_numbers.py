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