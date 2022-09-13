from abc import ABC, abstractmethod

class Talker(ABC):
    @abstractmethod
    def talk(self):
        pass


class Knigget(Talker):
    def talk(self):
        print("Ni!")

k = Knigget()
print(isinstance(k, Talker))
k.talk()
print()

##########################
class Herring:
    def talk(self):
        print("Blub.")

h = Herring()
print(isinstance(h, Talker))
print(Talker.register(Herring))
print(isinstance(h, Talker))
print(issubclass(Herring, Talker))
print()

##########################
class Clam:
    pass

print(Talker.register(Clam))
print(issubclass(Clam, Talker))
c = Clam()
print(isinstance(c, Talker))
c.talk()
