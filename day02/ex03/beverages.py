class HotBeverage:
    def __init__(self):
        self.name = "hot beverage"
        self.price = 0.30

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self):
        return f'name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}'


class Coffee(HotBeverage):
    def __init__(self):
        self.name = "coffee"
        self.price = 0.40
        
    def description(self):
        return "A coffee, to stay awake."


class Tea(HotBeverage):
    def __init__(self):
        super().__init__()
        self.name = "tea"
        self.price = 0.30



class Chocolate(HotBeverage):
    def __init__(self):
        self.name = "chocolate"
        self.price = 0.50
        
    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self):
        self.name = "cappuccino"
        self.price = 0.45

    def description(self):
        return "Un po’ di Italia nella sua tazza!"       


def test():
    hot_beverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()

    print("\n")
    print(hot_beverage.__str__())
    print("\n")
    print(coffee)
    print("\n")
    print(tea)
    print("\n")
    print(chocolate)
    print("\n")
    print(cappuccino)
    print("\n")    

if __name__ == '__main__':

    try:
        test()

    except Exception as e:
        print(e)