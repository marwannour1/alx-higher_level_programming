class test():
    def __init__(self, c=0):
        self.__c = c

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if value > 5:
            raise ValueError("Value must be less than 5")
        self.__c = value
    
class test2(test):
    def __init__(self):

        super().__init__()


if __name__ == "__main__":
    t = test(10)
    print(t.c)
    t.c = 17
  
