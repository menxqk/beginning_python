format = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print(format % values)
print()

from string import Template 
tmpl = Template("Hello, $who! $what enough for ya?")
print(tmpl.substitute(who="Mars", what="Dusty"))
print()

print("{}, {} and {}".format("first", "second", "third"))
print("{0}, {1} and {2}".format("first", "second", "third"))
print("{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to"))
print()

from math import pi
print("{name} is approximately {value:.2f}".format(value=pi, name="Pi"))
print("{name} is approximately {value}".format(value=pi, name="Pi"))
print()

from math import e
print(f"Euler's constant is roughly {e}.")
