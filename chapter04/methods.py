d = {
    'name': 'Gumby',
    'age': 42
}
print(d)
print('d.clear():', d.clear())
print(d)
print()

x = {'key': 'value'}
y = x
print('x:', x)
print('y:', y)
x = {}
print('x:', x)
print('y:', y)
x = {'key': 'value'}
y = x
x.clear()
print('x:', x)
print('y:', y)
x = {'key': 'value'}
print(x)
y = x.copy()
print('x:', x)
print('y:', y)
x.clear()
print('x:', x)
print('y:', y)
print()

x = dict.fromkeys(['name', 'age'])
y = dict.fromkeys(['name', 'age'], '(unknown)')
print('x:', x)
print('y:', y)
