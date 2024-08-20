class coffee_machine():
    def __init__(self):
        self.MENU = {
            'espresso' : {
                'ingredients':{'milk':50,
                            'water':100,
                            'coffee':18
                            },
                'cost':1
                                            
            },
            'cappaccino': {
                'ingredients':{'milk': 70,
                            'water':130,
                            'coffee':24},
                'cost':2
            },
            'latte': {'ingredients':{'milk':100,
                                    'water':50,
                                    'coffee':30},
                    'cost':1.5             
            }
        }
        self.resources = {'milk':400,
                    'water': 500,
                    'coffee': 100}
        self.profit = 0

    def resourse_req(self,order):
        for item in order:
            if order[item] > self.resources[item]:
                print('sorry not enough resources...')
                return False
        return True

    def process_coin(self):
        total = int(input('how many quaters : '))*0.25
        total += (int(input('how many dimes : '))*0.10)
        total+=(int(input('how many pennis : '))*0.05)
        return total

    def transaction(self,taken_money,order_cost):
        if taken_money >= order_cost:
            change = round(taken_money-order_cost,2)
            print(f'your change : {change}')
            self.profit +=(taken_money - change)
            return True
        else:
            print(f'sorry not enough cost....{taken_money} will be refund...')
            return False

    def make_coffee(self,drink_name,ingredient):
        for item in ingredient:
            self.resources[item] -=ingredient[item]
        print(f'your {drink_name} is ready ....enjoy')
    def game(self):
        is_on = True

        while is_on:
            choice = input('what you want?...espresso/cappaccino/latte : ')
            if choice == 'off':
                is_on = False
            elif choice == 'report':
                print(f'milk : {self.resources["milk"]}ml')
                print(f'water : {self.resources["water"]}ml')
                print(f'coffee : {self.resources["coffee"]}g')
                print(f'total profit : {self.profit}')
            else:
                drink = self.MENU[choice]
                if self.resourse_req(drink['ingredients']) :
                    self.payment = self.process_coin()
                if self.transaction(self.payment,drink['cost']):
                    self.make_coffee(choice,drink['ingredients']) 

                    
coffee_machine().game()
                




