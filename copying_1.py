s = [1, 2, 3, 4, 5]
t = 6, 7, 8, 9, 10

#   1A)
cp1 = []
for e in s:
    cp1.append(e)

#   1B)
cp2 = [e for e in s]

#   2)  cannot do this for immutable types
cp3 = s.copy()

#   3)
cp4 = s[:]

#   4)
cp5 = list(s)

# there is no need to make copies out of immutable types like tuple, string






