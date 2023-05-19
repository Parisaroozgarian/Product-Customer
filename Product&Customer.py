class product:
    def __init__(self,id,name,type,price):
        self.__id=id
        self.__name=name
        self.__type=type
        self.__price=price

    def show(self):
        print('Name of Product: '+self.__name)
        print('Type of Product: '+self.__type)
        print('Price of Product: '+str(self.__price))

    def getprice(self):
        return self.__price

class Customer:
    def __init__(self,id,name,family,address):
        self.__id=id
        self.__name=name
        self.__family=family
        self.__address=address
        self.p1=product(100,'Apple','Iphone',1700)

    def show(self):
        print(self.__name+','+self.__family)

    def shopping(self):
        self.p1.show()
        a=int(input('Enter $:'))
        if(a>self.p1.getprice()):
            print('Ok , You Bought')
        else:
            print('I am sorry')

c1=Customer(1,'a','b','c')
c2=Customer(2,'a2','b2','c2')
lc=[c1,c2]
c1.shopping()