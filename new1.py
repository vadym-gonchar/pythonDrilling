a = int(input())

my_list = []

for i in range(a):
    b = int(input())
    for j in range(b):
        name = input().split()
        if name[1] == '5':
            my_list.append(True)
        else: my_list.append(False)
    print(my_list)
print(my_list)
if any(my_list):
    print('YES')
else:
    print('NO')








