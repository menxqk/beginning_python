x = 1
while x <= 100:
    print(x, end=' ')
    x += 1
print()
print()

words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)
print()

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print(number, end=' ')
print()
print()

x = list(range(0, 10))
print(x)
for i in range(0, len(x)):
    print(i, end=' ')
print()
print()

d = {'x': 1, 'y': 2, 'z': 3}
print(d)
for key in d:
    print(key, end=' ')
print()
for key, value in d.items():
    print(key, 'corresponds to', value)
print()

print(sorted([4, 3, 6, 8, 3]))
