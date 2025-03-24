import random

file = open('lines.txt', 'r', encoding='utf-8')

print(random.choice(file.readlines()))

file.close()