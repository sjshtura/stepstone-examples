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
    def __init__(self, name = None):
        if str(name) == name:
            self.__name = name
        else:
            self.__name = 'Marvin'

    name_counter = 0

    # name getter
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

x = Robot(17)
x.hi()
x.name = 'Hildy'
x.hi()
x.name = 17
x.hi()










