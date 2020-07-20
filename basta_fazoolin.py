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

    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            total += self.items[item]
        return total


class Franchise:

    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return 'This store is located at {}'.format(self.address)

    def available_menus(self, time):
        items = []
        for name in self.menus:
            if name.start_time <= time <= name.end_time:
                for item in name.items:
                    items.append(item)
        return items


class Business:

    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# Create Menus
brunch = Menu('Brunch', {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50,
                         'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 1100, 1600)
early_bird = Menu('early_bird', {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
                                 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
                                 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 1500, 1800)
dinner = Menu('Dinner', {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00,
                         'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50,
                         'coffee': 2.00, 'espresso': 3.00}, 1700, 2300)
kids = Menu('Kids', {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 1100 , 2100)
arepas_menu = Menu('Take a’ Arepa', {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00,
                                     'jamon arepa': 7.50}, )

# Create Franchises
flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids])
new_installment = Franchise('12 East Mulberry', [brunch, early_bird, dinner, kids])

# Create Businesses
business = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])

# Test if printing Menu.__repr__ will return string '{menu} menu available from {start_time} to {end_time}'
# print(brunch)

# Test if Menu.calculate_bill will print the total for items in [purchased_items]
# print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
# print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

# Test what menu items are available at certain times
# print(flagship_store.available_menus(1200))
