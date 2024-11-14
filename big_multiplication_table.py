# جدول ضرب گنده
# https://quera.org/problemset/3409

n = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        print(i*j,end = " ")
    print("\n")

# n = int(input())

# for i in range (1,n+1):

#     a = str(i)

#     for j in range (2,n+1):
#         b = " " + str(i * j)
#         a = a + b
#         # a = a + " " + str(i * j)

#     print(a)
    