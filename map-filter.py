coffe_menu = ["espresso","mocha","latte","cappuccino","americano","cortado","flat white"]


def find_coffee(coffee):
    """Finds the index of a coffee in the menu.

    [IMPLEMENT ME]
        1. Use the map function to create a list of lowercase coffee names from the menu.
        2. Use the index method to find the index of the given coffee in the list of lowercase names.
        3. Return the index.

    Args:
        coffee (str): The name of the coffee to find.
    """

    if coffee[0]=="c":
        return coffee

# map_coffee = map(find_coffee, coffe_menu)

# print(map_coffee)

# for x in map_coffee:
#     print(x)

filter_coffee = filter(find_coffee, coffe_menu)
print(filter_coffee)

for x in filter_coffee:
    print(x)