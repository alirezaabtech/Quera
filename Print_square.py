# چاپ مربع
# https://quera.org/problemset/591

side_length = int(input())
stars = "*"

print(stars * side_length)
for i in range(side_length-2):
    in_square = "*"
    for j in range(side_length-2):              #in_square += " " * side_lenght-2
        in_square += " "
    in_square += "*"
    print(in_square)

print(stars * side_length)