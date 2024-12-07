# خُب باقر سرما خورده
# https://quera.org/problemset/10231

line_number = ""
for i in range(5):
    str_input = input()
    if "MOLANA" in str_input or "HAFEZ" in str_input:
        line_number += str(i+1) + " "

if line_number == "":
    print("NOT FOUND!")
    
else:
    print(line_number)