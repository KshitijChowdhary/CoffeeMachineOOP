from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
    choice = input(f"What would you like? {menu.get_items()}\n")
    if choice == "latte" or choice == "cappuccino" or choice == "espresso":
        choice = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(choice):
            if money_machine.make_payment(choice.cost):
                coffee_maker.make_coffee(choice)

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        is_on = False





