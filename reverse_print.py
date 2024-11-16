# چاپ برعکس
# https://quera.org/problemset/3405?tab=submissions

inputs_list =[]
while True:
    inputs = int(input())
    if inputs == 0:
        break
    inputs_list.append(inputs)

inputs_list.reverse()
for i in inputs_list:
    print(i)