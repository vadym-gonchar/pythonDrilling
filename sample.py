lst = [1, 2, 3, 4, 5]

a = [i if i % 2 == 0 else print('hi') for i in lst ]
print(a)