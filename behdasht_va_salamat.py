# بهداشت و سلامت
# https://quera.org/problemset/51865

def final_grade(x,y):
    if y == 0:
        return 20
    elif y == 7:
        return x
    else:
        if x-y <= 0:
            return 0
        else:
            return x-y
norooz_current_score = int(input())
travel_time = int(input())

print(final_grade(norooz_current_score,travel_time))