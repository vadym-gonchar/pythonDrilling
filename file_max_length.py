
result = []
maximum = 0
with open('input.txt', encoding='utf-8') as inf:
    for line in inf:
        if len(line) > maximum:
            maximum = len(line)
            result.clear()
            result.append(line.strip())
        elif len(line) == maximum:
            result.append(line.strip())
print(*result, sep='\n')



