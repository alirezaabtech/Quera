# عدد چاپ‌کن
# https://quera.org/problemset/9774

input = input()

for i in input:
    digit_to_print = ""
    for _ in range(int(i)):
        digit_to_print += i

    print(i + ": " + digit_to_print)


# input = input()

# for i in range(len(input)):
#     digit = int(input[i])
    
#     digits_to_print =  str(digit) + ': '
#     for j in range(digit):
#         digits_to_print += str(digit)

#     print(digits_to_print)