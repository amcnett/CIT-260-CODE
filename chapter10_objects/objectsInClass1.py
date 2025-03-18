# Inclass Activity 1 on Objects and Classes
class MyMath:
    def __init__(self):
        self.__numOne = 0
        self.__numTwo = 0

    def getNumOne(self):
        return self.__numOne
    
    def getNumTwo(self):
        return self.__numTwo
    
    def setNumOne(self, num):
        self.__numOne = num
    
    def setNumTwo(self, num):
        self.__numTwo = num

    def __str__(self):
        return f"numOne is {self.__numOne} and numTwo is {self.__numTwo}"

    @staticmethod # decorator example
    def test():
        print("test")

def main():
    obj1 = MyMath()
    obj1.setNumOne(5)
    obj1.setNumTwo(10)
    #print(f"Object one holds {obj1.getNumOne()} and {obj1.getNumTwo()}")
    print(obj1)
    obj1.test()

    obj2 = MyMath()
    obj2.setNumOne(9)
    obj2.setNumTwo(3)
    print(obj2)
    #print(f"Object one holds {obj2.getNumOne()} and {obj2.getNumTwo()}")

if __name__ == '__main__':
    main()
    