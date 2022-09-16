class Foobar:
    def __init__(self, value=42):
        self.somevar = value


f = Foobar()
print(f.somevar)
print()

################################
class A:
    def hello(self):
        print("Hello, I'm A.")

class B(A):
    pass

class C(A):
    def hello(self):
        print("Hello, I'm C.")

a = A()
a.hello()
b = B()
b.hello()
c = C()
c.hello()
