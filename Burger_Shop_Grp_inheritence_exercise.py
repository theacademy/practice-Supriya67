# [Supriya, Samuele, Anabil]
# [05-09-2024]

class FoodItem:
    def __init__(self) -> None:
        self.name = ""
        self.price = 0.0
        # self.quantity = 0
    
    def __str__(self):
        return f"""
                {self.name}, 
                {self.price}
            """


class Burger(FoodItem):
    def __init__(self, type, size="r") -> None:
        super().__init__()
        self.name = "Burger"
        self.type = type
        self.size = size
        self.price = 10.0 if self.size == "r" else 12.0
        # self.types_list = ["beef", "chicken", "vegan"]

        match(self.type):
            case 'beef':
                self.price += 4.0
            case 'chicken':
                self.price += 2.0
            case 'vegan':
                self.price += 3.0


class Drink(FoodItem):
    def __init__(self, type, size='r') -> None:
        super().__init__()
        self.name = "Drink"
        self.type = type
        self.size = size
        self.price = 2.0 if self.size == "r" else 3.0

        match(self.type):
            case "pepsi":
                self.price += 0.5
            case "cola":
                self.price += 0.5
            case "fanta":
                self.price += 1.0
            

class Side(FoodItem):
    def __init__(self, type, size='r') -> None:
        super().__init__()
        self.name = "Side"
        self.type = type
        self.size = size
        self.price = 4.0 if self.size == "r" else 5.0

        match(self.type):
            case "fries":
                self.price += 0.5
            case "onion-rings":
                self.price += 1.0
            case "salad":
                self.price += 0.5
            

class Combo(FoodItem):
    def __init__(self, burger: Burger, drink: Drink, side: Side) -> None:
        super().__init__()
        self.name = "Combo"
        self.burger = burger
        self.drink = drink
        self.side = side
        self.price = self.burger.price + self.drink.price + self.side.price


class Order:
    def __init__(self) -> None:
        self.food_items_list = []

    def __str__(self):

        output = ''

        for food_item in self.food_items_list:

            if food_item.name == 'Combo':
                burger_output = f"Name: {food_item.burger.name}, Type: {food_item.burger.type}, Size: {food_item.burger.size}, Price: £{food_item.burger.price}"
                drink_output = f"Name: {food_item.drink.name}, Type: {food_item.drink.type}, Size: {food_item.drink.size}, Price: £{food_item.drink.price}"
                side_output = f"Name: {food_item.side.name}, Type: {food_item.side.type}, Size: {food_item.side.size}, Price: £{food_item.side.price}"
                output += f"Combo Items:\n--------------------\n{burger_output}\n{drink_output}\n{side_output}\nCombo Price: £{food_item.price}\n_________________________\n"
            else:
                output += f"Name: {food_item.name}, Type: {food_item.type}, Size: {food_item.size}, Price: {food_item.price}"
                output += '\n_________________________\n'

        return output
        
    def add_food_item(self, food_item):
        self.food_items_list.append(food_item)

    def clear_order(self):
        self.food_items_list = []

    def is_order_empty(self):
        return len(self.food_items_list) == 0

    def calculate_total_price(self):
        return sum([food_item.price for food_item in self.food_items_list])
    



def get_type_and_size_from_user(food_item_name):
    food_item_type = input(f"Enter your {food_item_name} choice: 1 - 3 -> ")
    food_item_size = input(f"Enter your {food_item_name} preferred size: regular (r) or large (l) -> ")
    # quantity = input(f"Enter your {food_item_name} preferred quantity -> ")
    return food_item_type, food_item_size


def user_input_burger():
    print("""
        BURGERS (available in regular or large size)
        ----------------
        1. Beef
        2. Chicken
        3. Vegan
        """)
    
    burger_type, burger_size = get_type_and_size_from_user("burger")
    burger_types_map = {'1':'beef', '2':'chicken', '3':'vegan'}
    b = Burger(type=burger_types_map[burger_type], size=burger_size)
    return b


def user_input_drink():
    print("""
        DRINKS (available in regular or large size)
        ----------------
        1. Pepsi
        2. Coca Cola
        3. Fanta
        """)
    
    drink_type, drink_size = get_type_and_size_from_user("drink")
    drink_types_map = {'1':'pepsi', '2':'cola', '3':'fanta'}
    d = Drink(type=drink_types_map[drink_type], size=drink_size)
    return d


def user_input_side():
    print("""
        SIDES (available in regular or large size)
        ----------------
        1. Fries
        2. Onion Rings
        3. Salad
        """)
    
    side_type, side_size = get_type_and_size_from_user("side")
    side_types_map = {'1':'fries', '2':'onion-rings', '3':'salad'}
    s = Side(type=side_types_map[side_type], size=side_size)
    return s


def user_input_combo():
    print("""
        COMBO
        -------------
        Includes a burger, a drink, and a side.
        """)
    b = user_input_burger()
    d = user_input_drink()
    s = user_input_side()
    c = Combo(b, d, s)
    return c


def take_order():
    order = Order()
    user_name = input("Welcome to the Burger Shop! Enter your name: ")
    keep_ordering = True

    while keep_ordering:
        actions = """
                1. Add burger
                2. Add drink
                3. Add side
                4. Add combo
                5. Finish order
                6. Cancel order
            """
        print(actions)

        user_action = input("Enter your choice: ")
        if user_action == '1':
            b = user_input_burger()
            order.add_food_item(b)
        if user_action == '2':
            d = user_input_drink()
            order.add_food_item(d)
        if user_action == '3':
            s = user_input_side()
            order.add_food_item(s)
        if user_action == '4':
            c = user_input_combo()
            order.add_food_item(c)
        if user_action == '5':
            keep_ordering = False
            print(f'Thank you for ordering {user_name}!')
        if user_action == '6':
            keep_ordering = False
            order.clear_order()
            print('Go back home and never come back!')
            
    if not order.is_order_empty():
        print('...summary of order...')
        print(order)
        print(f"Total cost for {user_name}'s order: £{order.calculate_total_price()}")


take_order()