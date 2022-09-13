def print_params1(*params):
    print(params)
print_params1(1, 2, 3, 4, 5)
print()

def print_params2(x, *y, z):
    print(x, y, z)
print_params2(1, 2, 3, 4, 5, z=7)
print()

def print_params3(**params):
    print(params)
print_params3(x=1, y=2, z=3, w=4)
