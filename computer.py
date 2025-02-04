class Computer:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, processor:str, Hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.proc = processor
        self.hdc = Hard_drive_capacity
        self.mem = memory
        self.os = operating_system
        self.year = year_made
        self.price = price
    def update(self):
        if self.os == 'Low Sierra':
            self.os = 'High Sierra'
        elif self.os == 'Windows 10':
            self.os = 'Windows 13'
        elif self.os == 'High Sierra' or self.os == 'Windows 13':
            print('It already has the latest software')
        else:
            print('Updates to this software are not supported')
    def change_price(self):
        if self.year <= 2000:
            self.price = 0
        elif self.year > 2000 and self.year <= 2020:
            discount_factor = 1000*(20-(self.year - 2000))
            self.price -= discount_factor
        else:
            upsell_factor = 100*(self.year-2000)
            self.price += upsell_factor
            
        

    
        






    # What methods will you need?