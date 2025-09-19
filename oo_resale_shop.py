from computer import *

class ResaleShop:

    """ inventory: a list where we'll store our inventory """
    inventory = []
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        computer_instance = computer
        return computer_instance

    """
    Takes in a computer instance, adds the associated computer
    """
    def buy(self, inventory, computer_instance):
        inventory.append(computer_instance)


    """
    Takes in a computer instance, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, inventory, computer_instance):
        computer_instance = self
        if computer_instance is not None:
            inventory.remove(computer_instance)
            print("Item", computer_instance.description, "sold!")
        else: 
            print("Item", computer_instance.description, "not found. Please select another item to sell.")

    """
    Takes in a computer instance and a new price, updates the price of the associated
    computer if it is the inventory, prints error message otherwise
    """ 
    def update_price(self, new_price:float, computer_instance):
        if computer_instance.price is not None:
            computer_instance.price ["price"] = new_price
        else:
            print("Item", computer_instance.description, "not found. Cannot update price.")

    """
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    
    def print_inventory(self, inventory, computer_instance):
        # If the inventory is not empty
        if inventory:
            # For each item
            for item in inventory:
                # Print its details
                print(f'Item ID: {inventory.index(item)} : {item}')
        else:
            print("No inventory to display.")

def main():
    ResaleShop.buy({"description":"2019 MacBook Pro", "processor_type":"Intel", "hard_drive_capacity":256, "memory":16, "operating_system":"High Sierra", "year_made":2019, "price":1000})
    ResaleShop.print_inventory()

if __name__ == "__main__":
    main()