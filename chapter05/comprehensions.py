y = [x * x for x in range(11)]
print(y)
z = [x * x for x in range(11) if x % 3 == 0]
print(z)
w = [(x, y) for x in range(3) for y in range(3)]
print(w)
print()

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
a = [b + '+' + g for b in boys for g in girls if b[0] == g[0]]
print(a)
print()

squares = {i: "{} squared is {}".format(i, i**2) for i in range(10)}
print(squares)
print(squares[8])
