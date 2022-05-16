# Jacqueline Unciano, jdu5sq
# Partner: Charles Braff, drq6fj
# Description: A collection of functions to help with ordering food from cville restaurants

silk_thai = {"Vegetable Spring Roll": 4.95,
             "Crab Rangoon": 5.95,
             "Shrimp Rolls": 6.95,
             "Silk Spicy Ravioli": 6.95,
             "Duck Roll": 7.95,
             "Chicken Wings": 6.95,
             "Silk Basil Wings": 7.95}

mc_donalds = {"Crispy Chicken Sandwich": 4.29,
              "Crispy Chicken Sandwich Meal": 7.89,
              "Big Mac Meal": 8.69,
              "Double Quarter Pounder with Cheese Meal": 9.36,
              "10 Piece McNuggets": 529}

bodos_bagels = {"Turkey Breast": 3.95,
                "Smoked Turkey Breast": 4.05,
                "Roast Beef": 4.45,
                "Ham": 3.90}

all_cville_restaurants = {"Silk Thai": silk_thai,
                          "Mc Donalds": mc_donalds,
                          "Bodos Bagels": bodos_bagels}

def add_menu_item(dict, new_item, price):
    """
    :param dict: The name of the restaurant's dictionary
    :param new_item: The name of the item that you want to add
    :param price: The price of the new item that you are adding to the menu
    :return: Adds a new item to a restaurant's menu.
    """
    dict[new_item] = price

def calculate_order(dict, list, tip = 0.18):
    """
    :param dict: The name of the restaurant's dictionary
    :param list: The list of items that you are ordering
    :param tip: The amount of tip that you would like to give
    :return: Calculates how much a specific order of menu items would cost (including tax and tip)
    """
    sum_order = 0
    for i in range(0, len(list)):
        if list[i] in dict:
            sum_order += dict[list[i]]
        else:
            print("Sorry,", list[i], "is not available at this restaurant!")
    with_tax = sum_order * 1.06
    with_tip = (with_tax * tip) + with_tax
    return with_tip

def print_the_menu(dict):
    """
    :param dict: the name of the restaurant's dictionary
    :return: The full menu with prices
    """
    for i in dict:
        print(i,"-",dict[i])

def place_mega_order(mega_menu, order):
    """
    :param mega_menu: All the menus for cville restaurants
    :param order: Your order from multiple restaurants
    :return: The total amount you have to pay
    """
    sum_of_all = 0
    for i in order:
        restaurant_name = i
        sum_of_one = calculate_order(mega_menu[restaurant_name], order[restaurant_name])
        sum_of_all += sum_of_one
    return sum_of_all
