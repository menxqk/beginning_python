class Person:

    def set_name(self, name):
        self.name = name
    
    def get_name(self, name):
        return self.name
    
    def greet(self):
        print("Hello, world! I'm {}.".format(self.name))


foo = Person()
bar = Person()
foo.set_name('Luke Skywalker')
bar.set_name('Anakin Skywalker')
foo.greet()
bar.greet()
print()

###################################
class Class:
    def method(self):
        print('I have a self!')

def function():
    print("I don't...")

instance = Class()
instance.method()
instance.method = function
instance.method()
print()

###################################
class Bird:
    song = 'Squaawk!'
    def sing(self):
        print(self.song)

bird = Bird()
bird.sing()
print()

###################################
class Secretive:

    def __inaccessible(self):
        print("Bet you can't see me ...")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()

s = Secretive()
#s.__inaccessible()
s.accessible()
