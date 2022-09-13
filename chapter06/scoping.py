scope = vars()
print(scope)
print()

def local_scope():
    x = 1
    scope = vars()
    print(scope)
local_scope()
print()
