from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_list = Menu()
bank = MoneyMachine()
machine = CoffeeMaker()

def main():
    off = False
    while not off:
        options = coffee_list.get_items()
        user_choice = input(f"What would you like? ({options}): ").strip().lower()
        if user_choice == 'report':
            machine.report()
            bank.report()
        elif user_choice == 'off':
            off = True
        else:
            drink = coffee_list.find_drink(user_choice)
            if drink is not None:
                if machine.is_resource_sufficient(drink):
                    if bank.make_payment(drink.cost):
                        machine.make_coffee(drink)


if __name__ == '__main__':
    main()

