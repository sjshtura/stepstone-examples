def hi(obj):
    print("Hi, I am " + obj.__name)

class Robot:

    # object method
    def hi(self):
        print("Hi, I am " + self.name)

    # class method
    def laws():
        return "A robot should never..."

    # constructor
    def __init__(self, name = 'Marvin'):
        self.__name = name

    name_counter = 0

    @property
    def name(self):
        self.name_counter += 1
        return str(self.__name)

    @name.setter
    def name(self, new_name):
        if str(new_name) == new_name:
            self.__name = new_name
        # else:
        #     self.name = 'Marvin'

x = Robot('Suzy')
print(x.name_counter)
print(x.name)
print(x.name_counter)
x.name = 'Hildy'
x.hi()
print(x.name_counter)











