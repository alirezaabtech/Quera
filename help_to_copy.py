random_number, file_name = input().split(" ")
output = ""
for _ in range(int(random_number)):
    output += "copy of "

output += file_name
print(output)

######### OR #########

# random_number, file_name = input().split(" ")

# print("copy of "*int(random_number)+file_name)