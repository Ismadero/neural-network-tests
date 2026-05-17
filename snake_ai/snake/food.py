import random
import constants

class Food:
    def __init__(self, occupied, amount):
        """ Initializes the class by placing 'amount' food items in unoccupied cells. """
        self.foods = set()
        self.new_food(occupied, amount)

    def eat_food(self, coord):
        """ Remove food at the given coord. Returns True if food was there, False otherwise. """
        if coord in self.foods:
            self.foods.remove(coord)
            return True
        return False
        

    def new_food(self, occupied, amount):   
        """ Place 'amount' new food items in cells not occupied by the snake or existing food. """
        available = [(x,y) 
                     for x in range(constants.COLUMNS) 
                     for y in range(constants.ROWS) 
                     if (x, y) not in occupied 
                     and (x, y) not in self.foods]
        amount = min(amount, len(available))                                    
        chosen = random.sample(available,amount)                               
        self.foods.update(chosen)

    def get_foods(self):
        """ Return the set of current food positions. """
        return self.foods