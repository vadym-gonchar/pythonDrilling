file = open('prices.txt')

res_sum = 0

for line in file:
    current_line = line.split()
    res_sum = res_sum + int(current_line[1]) * int(current_line[2])
print(res_sum)

file.close()

# calculate 2 values from the file