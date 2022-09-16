class Rectangle(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setitem__(self, name, value):
        if name == 'size':
            self.width, self.height = value
        else:
            self.__dict__[name] = value
    
    def __getitem__(self, name):
        if name == 'size':
            return self.width, self.height
        else:
            raise AttributeError()

r = Rectangle()
r['size'] = (50, 100)
print(r['size'])

