def change(n):
    n[0] = 'Mr. Gumby'

names = ['Mrs. Entity', 'Mrs. Thing']
print(names)
change(names)
print(names)
print()

n = names[:]
print('n is names:', n is names)
print('n == names:', n == names)
print()

def inc(x): return x + 1
foo = 10
inc(foo)
print(foo)
foo = inc(foo)
print(foo)
