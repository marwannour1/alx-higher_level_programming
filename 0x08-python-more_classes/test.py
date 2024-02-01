class test():
    def __init__(self):
        self.__c = 3

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value
    
class test2(test):
    def __init__(self):

        super().__init__()


if __name__ == "__main__":
    t = test()
    t.c = 2
    print(t.c)
    t2 = test2()
    print(t2.c)
    t2.c = 5
    print(t2.c)
    print(t.c)
