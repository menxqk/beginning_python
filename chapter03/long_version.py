print("{{ceci n'est pas une replacement field}}".format())
print("{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3))
print("{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3))
print()

fullname = ["Alfred", "Smoketoomuch"]
print("Mr {name[1]}".format(name=fullname))
print()

import math
tmpl = "The {mod.__name__} module defines the value {mod.pi} for Pi"
print(tmpl.format(mod=math))
print()


print("The number is {num}".format(num=42))
print("The number is {num:f}".format(num=42))
print("The number is {num:b}".format(num=42))
print("{num:10}".format(num=3))
print("{name:10}".format(name="Bob"))
from math import pi
print("Pi day is {pi:.2f}".format(pi=pi))
print("{pi:10.2f}".format(pi=pi))
print("{:.5}".format("Guido van Rossum"))
print("{:010.2f}".format(pi))
