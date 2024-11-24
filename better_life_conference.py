# همایش زندگی بهتر
# https://quera.org/problemset/10325

row_number , seat_number = input().split(" ")
row_number = int(row_number)
seat_number = int(seat_number)
output_direction = ""
output_row = int()
output_seat = int()
if seat_number > 10:
    # print("Left" , end =" ")
    # print(10 - row_number + 1 , end =" ")
    # print(20 - seat_number + 1)
    output_direction = "Left"
    output_row = 11 - row_number
    output_seat = 21 - seat_number
else:
    # print("Right" , end =" ")
    # print(10 - row_number + 1 , end =" ")
    # print(seat_number)
    output_direction = "Right"
    output_row = 11 - row_number
    output_seat = seat_number

print(output_direction,output_row,output_seat)

######### OR #########

# row_number,seat_number = input().split(" ")

# n = "Left"
# b = 21 - int(seat_number)
# if int(seat_number) <=  10:
#     n = "Right"
#     b = int(seat_number)

# a = 11 - int(row_number)

# print(n,a,b)