"""
Supriya, Samuele, Anabil

Burger Shop
--------------------------------------------------------------------------------
Prices for each item:
- Burger: £10.00 (regular size) or £12.00 (large size)
    - Beef: £3.00 extra, Chicken: £3.00 extra, Vegan: £4.00 extra, Veggie: £2.00 extra
- Drink: £2.00 (regular size) or £3.00 (large size)
    - Pepsi: £0.50 extra, Coca Cola: £0.50 extra, Fanta: £1.00 extra, Coffee: £1.00 extra
- Side: £4.00 (regular size) or £5.00 (large size)
    - Fries: £0.50 extra, Onion Rings: £1.00 extra, Salad: £0.50 extra
- Combo: Burger + Drink + Side
"""

# Global Variables, can be changed according to our needs
BURGER_BASE_PRICE = 10.00
BURGER_TYPE_PRICE = {
    "Beef": 3.00,
    "Chicken": 3.00,
    "Vegan": 4.00,
    "Veggie": 2.00
}
BURGER_SIZE_PRICE = {
    "Regular": 0.00,
    "Large": 2.00
}

DRINK_BASE_PRICE = 2.00
DRINK_TYPE_PRICE = {
    "Pepsi": 0.50,
    "Coca Cola": 0.50,
    "Fanta": 1.00,
    "Coffee": 1.00
}
DRINK_SIZE_PRICE = {
    "Regular": 0.00,
    "Large": 1.00
}

SIDE_BASE_PRICE = 4.00
SIDE_TYPE_PRICE = {
    "Fries": 0.50,
    "Onion Rings": 1.00,
    "Salad": 0.50
}
SIDE_SIZE_PRICE = {
    "Regular": 0.00,
    "Large": 1.00
}

class FoodItem:
    def __init__(self, name, type, size, price) -> None:
        """
        Constructor for FoodItem class. Initializes the food item with the given name, type, size, and price.
        Inputs:
            name: str, name of the food item
            type: str, type of the food item
            size: str, size of the food item
            price: float, price of the food item
        Outputs: None
        """
        self.name = name
        self.type = type
        self.size = size
        self.price = price

    def __str__(self):
        """
        Display the food item details.
        Inputs: None
        Outputs: str, formatted string of the food item
        """
        return f"Name: {self.name}, Type: {self.type}, Size: {self.size}, Price: £{self.price:.2f}"

class Burger(FoodItem):
    def __init__(self, type, size, price) -> None:
        """
        Constructor for Burger class.
        Inputs:
            type: str, type of the burger
            size: str, size of the burger
            price: float, price of the burger
        Outputs: None
        """
        super().__init__("Burger", type, size, price)

class Drink(FoodItem):
    def __init__(self, type, size, price) -> None:
        """
        Constructor for Drink class.
        Inputs:
            type: str, type of the drink
            size: str, size of the drink
            price: float, price of the drink
        Outputs: None
        """
        super().__init__("Drink", type, size, price)

class Side(FoodItem):
    def __init__(self, type, size, price) -> None:
        """
        Constructor for Side class.
        Inputs:
            type: str, type of the side
            size: str, size of the side
            price: float, price of the side
        Outputs: None
        """
        super().__init__("Side", type, size, price)

class Combo(FoodItem):
    def __init__(self, burger, drink, side) -> None:
        """
        Constructor for Combo class.
        Inputs:
            burger: Burger, burger object
            drink: Drink, drink object
            side: Side, side object
        Outputs: None
        """
        self.burger = burger
        self.drink = drink
        self.side = side
        super().__init__("Combo", "None", "None", self.get_total_price())

    def get_total_price(self):
        """
        Computes the total price of the combo item, which is the sum of the prices of each food item
        (i.e. burger price + drink price + side price).
        Inputs: None
        Outputs: float, total price of the combo
        """
        return self.burger.price + self.drink.price + self.side.price
    
    def __str__(self):
        """
        Display the combo details differently compared to the other food item objects such as burger, drink and side.
        Inputs: None
        Outputs: str, formatted string of the combo
        """
        output = "Name: Combo (one burger, one drink, one side)\n" \
            + f"Combo Burger - {self.burger}\n" \
            + f"Combo Drink - {self.drink}\n" \
            + f"Combo Side - {self.side}\n" \
            + f"Total Combo Price: £{self.get_total_price():.2f}"
        return output
    
class Order:
    def __init__(self) -> None:
        """
        Constructor for Order class. Initializes an empty list to store food items.
        Inputs: None
        Outputs: None
        """
        self.food_items = []

    def add_item(self, item):
        """
        Add a food item to the order i.e., adds the item to the list.
        Inputs: item: FoodItem, food item object
        Outputs: None
        """
        self.food_items.append(item)

    def clear_order(self):
        """
        Clear the order i.e., remove all the food items from the list.
        Inputs: None
        Outputs: None
        """
        self.food_items = []

    def is_empty(self):
        """
        Check if the order is empty i.e., if the list of food items is empty.
        Inputs: None
        Outputs: bool, True if order is empty, False otherwise
        """
        return len(self.food_items) == 0
    
    def get_total_price(self):
        """
        Compute the total price of the order, which is the sum of the prices of all the food items in the order.
        Inputs: None
        Outputs: float, total price of the order
        """
        return sum([food_item.price for food_item in self.food_items])
    
def user_input_burger():
    """
    Asks the user for input and stores it in a burger object.
    Inputs: None
    Outputs: Burger, burger object
    """
    isTypeValid = False
    isSizeValid = False

    countErrors = 0
    while not isTypeValid:
        print("Please select the associated number for the type of burger: 1. Beef, 2. Chicken, 3. Vegan, 4. Veggie")
        burger_type = input()
        if burger_type in [str(i) for i in range(1, len(BURGER_TYPE_PRICE)+1)]:
            isTypeValid = True
            burger_type = list(BURGER_TYPE_PRICE.keys())[int(burger_type)-1]
        elif countErrors == 3:
            print("Too many invalid inputs. Returning to main menu.")
            return None
        else:
            countErrors += 1
            print("Invalid input. Please try again.")

    countErrors = 0
    while not isSizeValid:
        print("Please select the associated number for the size of burger: 1. Regular, 2. Large")
        burger_size = input()
        if burger_size in [str(i) for i in range(1, len(BURGER_SIZE_PRICE)+1)]:
            isSizeValid = True
            burger_size = list(BURGER_SIZE_PRICE.keys())[int(burger_size)-1]
        elif countErrors == 3:
            print("Too many invalid inputs. Returning to main menu.")
            return None
        else:
            countErrors += 1
            print("Invalid input. Please try again.")

    b = Burger(burger_type, burger_size, BURGER_BASE_PRICE + BURGER_TYPE_PRICE[burger_type] + BURGER_SIZE_PRICE[burger_size])
    return b
 
def user_input_drink():
    """
    Asks the user for input and stores it in a drink object.
    Inputs: None
    Outputs: Drink, drink object
    """ 
    isTypeValid = False
    isSizeValid = False

    countErrors = 0
    while not isTypeValid:
        print("Please select the associated number for the type of drink: 1. Pepsi, 2. Coca Cola, 3. Fanta, 4. Coffee")
        drink_type = input()
        if drink_type in [str(i) for i in range(1, len(DRINK_TYPE_PRICE)+1)]:
            isTypeValid = True
            drink_type = list(DRINK_TYPE_PRICE.keys())[int(drink_type)-1]
        elif countErrors == 3:
            print("Too many invalid inputs. Returning to main menu.")
            return None
        else:
            countErrors += 1
            print("Invalid input. Please try again.")

    countErrors = 0
    while not isSizeValid:
        print("Please select the associated number for the size of drink: 1. Regular, 2. Large")
        drink_size = input()
        if drink_size in [str(i) for i in range(1, len(DRINK_SIZE_PRICE)+1)]:
            isSizeValid = True
            drink_size = list(DRINK_SIZE_PRICE.keys())[int(drink_size)-1]
        elif countErrors == 3:
            print("Too many invalid inputs. Returning to main menu.")
            return None
        else:
            countErrors += 1
            print("Invalid input. Please try again.")

    d = Drink(drink_type, drink_size, DRINK_BASE_PRICE + DRINK_TYPE_PRICE[drink_type] + DRINK_SIZE_PRICE[drink_size])
    return d
 
def user_input_side():
    """
    Asks the user for input and stores it in a side object.
    Inputs: None
    Outputs: Side, side object
    """
    #ask user for input and store it in side object
    isTypeValid = False
    isSizeValid = False

    countErrors = 0
    while not isTypeValid:
        print("Please select the associated number for the type of side: 1. Fries, 2. Onion Rings, 3. Salad")
        side_type = input()
        if side_type in [str(i) for i in range(1, len(SIDE_TYPE_PRICE)+1)]:
            isTypeValid = True
            side_type = list(SIDE_TYPE_PRICE.keys())[int(side_type)-1]
        elif countErrors == 3:
            print("Too many invalid inputs. Returning to main menu.")
            return None
        else:
            countErrors += 1
            print("Invalid input. Please try again.")

    countErrors = 0
    while not isSizeValid:
        print("Please select the associated number for the size of side: 1. Regular, 2. Large")
        side_size = input()
        if side_size in [str(i) for i in range(1, len(SIDE_SIZE_PRICE)+1)]:
            isSizeValid = True
            side_size = list(SIDE_SIZE_PRICE.keys())[int(side_size)-1]
        elif countErrors == 3:
            print("Too many invalid inputs. Returning to main menu.")
            return None
        else:
            countErrors += 1
            print("Invalid input. Please try again.")
    
    s = Side(side_type, side_size, SIDE_BASE_PRICE + SIDE_TYPE_PRICE[side_type] + SIDE_SIZE_PRICE[side_size])
    return s
 
def user_input_combo():
    """
    Asks the user for input and stores it in a combo object.
    A combo must include one burger, one side, and one drink.
    Inputs: None
    Outputs: Combo, combo object
    """
    print("Combo selected...")
    b = user_input_burger()
    d = user_input_drink()
    s = user_input_side()
    if b and d and s:
        c = Combo(b, d, s)
    else:
        c = None

    return c
 
def take_order():
    """
    Main function to take the order from the user.
    Asks user for name for the order.
    Repeats taking order until client is done.
    Displays order details at the end.
    Displays a thank you message
    Inputs: None
    Outputs: None
    """
    order = Order()
    user_name = input("Welcome to the Burger Shop! Enter your name: ")
    keep_ordering = True

    while keep_ordering:
        actions = f"""
                What would you like to add to your order, {user_name}?
                1. Add burger
                2. Add drink
                3. Add side
                4. Add combo
                5. Finish order
                6. Cancel order
            """
        print(actions)

        user_input = input("Enter your choice: ")
        isUserInputValid = False
        while not isUserInputValid:
            if user_input in [str(i) for i in range(1, 7)]:
                isUserInputValid = True
            else:
                print("Invalid input. Please try again.")
                user_input = input("Enter your choice: ")

        if user_input == "1":
            b = user_input_burger()
            if b:
                order.add_item(b)
        elif user_input == "2":
            d = user_input_drink()
            if d:
                order.add_item(d)
        elif user_input == "3":
            s = user_input_side()
            if s:
                order.add_item(s)
        elif user_input == "4":
            c = user_input_combo()
            if c:
                order.add_item(c)
        elif user_input == "5":
            keep_ordering = False
        else:
            # user_input == 6 i.e. cancel order
            order.clear_order()
            print(f"Order cancelled for {user_name}.")
            return
    
    if order.is_empty():
        print(f"Order is empty for {user_name}.")
        return
    
    print(f"Order summary for {user_name}:")
    print("--------------------------------------------------------------------------------")
    for food_item in order.food_items:
        print(food_item)
        print("--------------------------------------------------------------------------------")
    print(f"Total Price for order: £{order.get_total_price():.2f}")
    print("Thank you for ordering from the Burger Shop!")
 
if __name__ == "__main__":
    take_order()