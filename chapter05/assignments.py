x, y, z = 1, 2, 3
print(x, y, z)
x, y = y, x
print(x, y, z)
values = x, y, z
print(values)
print()

scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
print(scoundrel)
print(scoundrel.popitem())
print(scoundrel)
print()

a, b, *rest = [1, 2, 3, 4]
print(a, b, rest)
print()

name = "Albus Percival Wulfric Brian Dubledore"
first, *middle, last = name.split()
print(first)
print(middle)
print(last)
