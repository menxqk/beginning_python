items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print('d:', type(d), d)
print('len(d):', len(d))
del d['name']
print(d)
