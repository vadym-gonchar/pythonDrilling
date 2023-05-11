#shallow copy
s = [[1,2], [3,4]]

cp = s.copy()

cp[1][0] = 100

print(s)
# [[1, 2], [100, 4]]
print(cp)
# [[1, 2], [100, 4]]

#deep copy
cp1 = [e.copy() for e in s]

cp1[0][0] = 300

print(s)
# [[1, 2], [100, 4]]
print(cp1)
# [[300, 2], [100, 4]]
