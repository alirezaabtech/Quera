# کامل بودن یا نبودن
# https://quera.org/problemset/282

n = int(input())
c = (n // 2) + 1
total = 0
for i in range(1,c):
    if n % i == 0:
        total += i

if total == n:
    print("YES")
else:
    print("NO")