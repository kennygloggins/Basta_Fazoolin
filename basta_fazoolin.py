# By: Kenny_G_Loggins
# Created on: 7/19/20, 7:29 PM
# File: basta_fazoolin.py
# Project: git_basfaz


class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return '{} menu available from {} to {}'.format(self.name, self.start_time, self.end_time)


brunch = Menu('Brunch', {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                         'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, '11am', '4pm')
early_bird = Menu('early_bird', {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                                 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
                                 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, '3pm', '6pm')
dinner = Menu('Dinner', {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00,
                         'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50,
                         'coffee': 2.00, 'espresso': 3.00}, '5pm', '11pm')
kids = Menu('Kids', {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, '11am', '9pm')

print(brunch)