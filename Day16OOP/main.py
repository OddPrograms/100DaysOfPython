# from turtle import Turtle, Screen
#
# def turtle():
#     michelangelo = Turtle()
#     michelangelo.shape("turtle")
#
#     my_screen = Screen()
#     my_screen.canvheight = 1080
#     my_screen.canvwidth = 1920
#     michelangelo.color("orange")
#     michelangelo.forward(100)
#
#     print(my_screen)
#     my_screen.exitonclick()

# from prettytable import PrettyTable
# def tables():
#     table = PrettyTable()
#     table.add_column("Pokemon", ["Squirtle", "Bublasaur", "Charmander"])
#     table.add_column("Type", ["Water", "Grass", "Fire"])
#     table.align = "l"
#     print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()
    is_on = True

    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? {options}: ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)

if __name__ == '__main__':
    main()