import random

from beverages import Cappuccino, Chocolate, Coffee, HotBeverage, Tea


class EmptyCup(HotBeverage):
    def _init_(self):
        super().__init__()
        self.name = "empty cup"
        self.price = 0.90
        self.description = "An empty cup?! Gimme my money back!"


class BrokenMachineException(Exception):
    def __init__(self):
        super().__init__("This coffee machine has to be repaired.")


class CoffeeMachine:
    def __init__(self):
        self.drinks_served = 0
        self.is_broken = False

    def repair(self):
        self.is_broken = False

    def serve(self, drink):
        if self.is_broken:
            raise BrokenMachineException()

        self.drinks_served += 1
        if self.drinks_served > 10:
            self.is_broken = True
            self.drinks_served = 0

        return random.choice([drink, EmptyCup()])


def test():
    coffee_machine = CoffeeMachine()
    hot_beverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()

    for _ in range(15):
        try:
            drink = coffee_machine.serve(random.choice([hot_beverage, coffee, tea, chocolate, cappuccino]))
            print('\n')
            print(drink)
        except BrokenMachineException:
            print('\n')
            print("The coffee machine is broken. Time to repair!")
            coffee_machine.repair()    

if __name__ == '__main__':

    try:
        test()
    except Exception as e:
        print(e)