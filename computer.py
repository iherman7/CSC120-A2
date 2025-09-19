class computer:

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int


    def __init__(self, desc:str, processor:str, hard_drive:int, memory:int, os:int, year:int):
        self.description = desc
        self.processor_type = processor
        self.hard_drive_capacity = hard_drive
        self.memory = memory
        self.operating_system = os
        self.year_made = year

    """
    changes computer's price based on the year it was made, and updates the computer's operating system
    if it does not have a new one
    """
    def refurbish(self, new_os:str):
        if self is not None:
            computer = self # locate the computer
            if int(self.year_made) < 2000:
                self.price = 0 # too old to sell, donation only
            elif int(self.year_made) < 2012:
                self.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(self.year_made) < 2018:
                self.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                self.price = 1000 # recent stuff

            if new_os is not None:
                self.operating_system = new_os # update details after installing new OS
        else:
            print("Item", self, "not found. Please select another item to refurbish.")