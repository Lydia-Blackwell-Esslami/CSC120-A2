class ResaleShop:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, account:int, inventory:list):
        self.funds = account
        self.inventory = inventory
    
    def buy_computer(self, computer):
        self.inventory.append(computer)
        self.funds -= computer.price
    
    def sell_computer(self, computer_index: int):
        computer = self.inventory[computer_index]
        self.funds += computer.price
        self.inventory.pop(computer_index)

    def check_inventory(self):
        for item in self.inventory:
            print(item)



    # What methods will you need?