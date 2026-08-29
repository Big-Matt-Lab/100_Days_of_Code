from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_list = Menu()
bank = MoneyMachine()
machine = CoffeeMaker()


def main():
    off = False
    while not off:
        user_choice = (
            input(
                "What would you like? (espresso $1.50, latte $2.50, cappuccino $3.00): "
            )
            .strip()
            .lower()
        )
        if user_choice == "report":
            machine.report()
            bank.report()
        elif user_choice == "off" or user_choice not in coffee_list.get_items():
            off = True
        else:
            order = coffee_list.find_drink(user_choice)
            print(order)
            print("Coffee Time!")
            if machine.is_resource_sufficient(order):
                if bank.make_payment(order.cost):
                    machine.make_coffee(order)


if __name__ == "__main__":
    main()
