if False == False:
     print("False == False")
if bool(None) == False:
    print("bool(None) == False")
if bool(0) == False:
    print("bool(0) == False")
if bool("") == False:
    print("bool(\"\") == False")
if bool(()) == False:
    print("bool(()) == False")
if bool([]) == False:
    print("bool([]) == False")
if bool({}) == False:
    print("bool({}) == False")
print()

print("bool('I think, therefore I am'):", bool('I think, therefore I am'))
print("bool(42):", bool(42))
print("bool(''):", bool(''))
print("bool(0):", bool(0))
