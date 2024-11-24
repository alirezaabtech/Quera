# دو نقطه خط
# https://quera.org/problemset/3414


def find_the_location(x1,y1,x2,y2):
    if y1 == y2:
        return "Horizontal"
    elif x1 == x2:
        return "Vertical"
    else:
        return "Try again"

mustafa_column_number,mustafa_line_number,boss_column_number,boss_line_number = input().split(" ")

print(find_the_location(mustafa_column_number,mustafa_line_number,boss_column_number,boss_line_number))