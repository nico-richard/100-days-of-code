MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

INITIAL_RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

COINS_VALUE = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.1,
    "quarter": 0.25,
}


class CoffeMachine:
    def __init__(self):
        self.COINS_VALUE = COINS_VALUE
        self.resources = INITIAL_RESOURCES
        self.MENU = MENU
        self.command = ''

    def get_stock(self):
        for resource, quantity in self.resources.items():
            print(f'{resource} : {quantity}', end=' ')
            if resource == 'coffee':
                print('g')
            else:
                print('ml')

    def user_input(self):
        self.command = input(
            'What would you like ? (espresso [e] / latte [l] / cappuccino [c]) : ')
        self.process_command()

    def process_command(self):
        match self.command:
            case 'e' | 'expresso':
                self.prepare('espresso')
            case 'l' | 'latte':
                self.prepare('latte')
            case 'c' | 'cappuccino':
                self.prepare('cappuccino')
            case 'r' | 'report':
                self.get_stock()
            case 'q' | 'quit':
                pass
            case _:
                print('wrong command')
                self.user_input()

    def check_resources(self, drink):
        for ingredient, quantity_required in self.MENU[drink]['ingredients'].items():
            if self.resources[ingredient] < quantity_required:
                print(f'Sorry, there is not enough {ingredient}')
                return

    def get_money(self, drink):
        cost = self.MENU[drink]["cost"]

        print(f'Cost : ${cost}')
        print('Please insert coins')

        coins_used = {}
        total = 0
        for coinType, value in self.COINS_VALUE.items():
            coins_used[coinType] = int(input(f'How many {coinType} ? '))
            total += value * coins_used[coinType]

        print(f'You have entered : ${round(total, 2)}')
        if total < cost:
            remaining_money = round(cost - total, 2)
            print(
                f'There is not enough money, missing {remaining_money}')
            return False
        print(f'Here is ${round(total - cost, 2)} in change')

    def prepare(self, drink):
        self.check_resources(drink)
        if not self.get_money(drink):
            print('Please retry')
            return

        for ingredient, quantity in self.MENU[drink]['ingredients'].items():
            self.resources[ingredient] -= quantity

        print(f'Here is your {drink} ☕')
        self.user_input()

    def run(self):
        while self.command != 'q':
            self.user_input()


coffeMachine = CoffeMachine()
coffeMachine.run()
