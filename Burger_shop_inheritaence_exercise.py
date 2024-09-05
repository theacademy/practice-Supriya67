'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

# Name: [Supriya, Samuele, Anabil]
# Date: 2024-09-05

class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Burger(FoodItem):
    def __init__(self, name, price, patty_type, toppings):
        super().__init__(name, price)
        self.patty_type = patty_type
        self.toppings = toppings

    def __str__(self):
        return (f"Burger: {self.name}, Patty: {self.patty_type}, "
                f"Toppings: {', '.join(self.toppings)}, Price: ${self.price:.2f}")


class Drink(FoodItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return f"Drink: {self.name}, Size: {self.size}, Price: ${self.price:.2f}"


class Side(FoodItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return f"Side: {self.name}, Size: {self.size}, Price: ${self.price:.2f}"


class Combo(FoodItem):
    def __init__(self, name, burger, side, drink):
        combo_price = burger.price + side.price + drink.price - 2.00  # $2 discount for combo
        super().__init__(name, combo_price)
        self.burger = burger
        self.side = side
        self.drink = drink

    def __str__(self):
        return (f"Combo: {self.name}\n{self.burger}\n{self.side}\n{self.drink}\n"
                f"Total Combo Price: ${self.price:.2f}")


class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        return sum(item.price for item in self.items)

    def __str__(self):
        order_details = "\n".join(str(item) for item in self.items)
        return (f"Order for {self.customer_name}:\n{order_details}\n"
                f"Total Price: ${self.total_price():.2f}")


# User input functions with fixed prices
def user_input_burger():
    print("Burger Options:")
    print("1. Classic (£5.99)")
    print("2. Cheese (£6.49)")
    print("3. Double (£7.99)")
    print("4. Veggie (£5.49)")

    choice = input("Select a burger (1-4): ")
    if choice == "1":
        return Burger("Classic", 5.99, "Beef", ["Lettuce", "Tomato", "Onion"])
    elif choice == "2":
        return Burger("Cheese", 6.49, "Beef", ["Lettuce", "Cheese", "Pickles"])
    elif choice == "3":
        return Burger("Double", 7.99, "Double Beef", ["Lettuce", "Cheese", "Tomato", "Onion"])
    elif choice == "4":
        return Burger("Veggie", 5.49, "Veggie", ["Lettuce", "Tomato", "Onion"])
    else:
        print("Invalid choice.")
        return None

def user_input_drink():
    print("Drink Options:")
    print("1. Soda (Small £1.99, Medium £2.49, Large £2.99)")
    print("2. Lemonade (Small £2.49, Medium £2.99, Large £3.49)")
    print("3. Iced Tea (Small £1.99, Medium £2.49, Large £2.99)")

    choice = input("Select a drink (1-3): ")
    size = input("Choose size (small, medium, large): ").lower()

    if choice == "1":
        if size == "small":
            return Drink("Soda", 1.99, "Small")
        elif size == "medium":
            return Drink("Soda", 2.49, "Medium")
        elif size == "large":
            return Drink("Soda", 2.99, "Large")
    elif choice == "2":
        if size == "small":
            return Drink("Lemonade", 2.49, "Small")
        elif size == "medium":
            return Drink("Lemonade", 2.99, "Medium")
        elif size == "large":
            return Drink("Lemonade", 3.49, "Large")
    elif choice == "3":
        if size == "small":
            return Drink("Iced Tea", 1.99, "Small")
        elif size == "medium":
            return Drink("Iced Tea", 2.49, "Medium")
        elif size == "large":
            return Drink("Iced Tea", 2.99, "Large")
    else:
        print("Invalid choice.")
        return None

def user_input_side():
    print("Side Options:")
    print("1. Fries (Small £2.49, Medium £3.49, Large £4.49)")
    print("2. Onion Rings (Small £2.99, Medium £3.99, Large £4.99)")
    print("3. Garden Salad (Small £3.49, Medium £4.49, Large £5.49)")

    choice = input("Select a side (1-3): ")
    size = input("Choose size (small, medium, large): ").lower()

    if choice == "1":
        if size == "small":
            return Side("Fries", 2.49, "Small")
        elif size == "medium":
            return Side("Fries", 3.49, "Medium")
        elif size == "large":
            return Side("Fries", 4.49, "Large")
    elif choice == "2":
        if size == "small":
            return Side("Onion Rings", 2.99, "Small")
        elif size == "medium":
            return Side("Onion Rings", 3.99, "Medium")
        elif size == "large":
            return Side("Onion Rings", 4.99, "Large")
    elif choice == "3":
        if size == "small":
            return Side("Garden Salad", 3.49, "Small")
        elif size == "medium":
            return Side("Garden Salad", 4.49, "Medium")
        elif size == "large":
            return Side("Garden Salad", 5.49, "Large")
    else:
        print("Invalid choice.")
        return None


def user_input_combo():
    print("Creating a Combo (Includes a burger, side, and drink with £2 discount):")
    burger = user_input_burger()
    if burger is None:
        return None
    side = user_input_side()
    if side is None:
        return None
    drink = user_input_drink()
    if drink is None:
        return None

    combo_name = input("Enter a combo name: ")
    return Combo(combo_name, burger, side, drink)


# Main function to take the order
def take_order():
    customer_name = input("Please enter your name: ")
    print(f"Welcome to the Burger Shop! {customer_name}")
    order = Order(customer_name)

    while True:
        print("\nMenu Options:")
        print("1. Add a Burger")
        print("2. Add a Drink")
        print("3. Add a Side")
        print("4. Add a Combo")
        print("5. Finish Order")
        print("6. Cancel Order")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            burger = user_input_burger()
            if burger:
                order.add_item(burger)
        elif choice == "2":
            drink = user_input_drink()
            if drink:
                order.add_item(drink)
        elif choice == "3":
            side = user_input_side()
            if side:
                order.add_item(side)
        elif choice == "4":
            combo = user_input_combo()
            if combo:
                order.add_item(combo)
        elif choice == "5":
            print("\nOrder Summary:")
            print(order)
            print("\nThank you for your order!")
            break
        elif choice == "6":
            print("\nOrder has been canceled. Thank you for visiting!")
            break
        else:
            print("Invalid option, please try again.")


# Run the ordering process
take_order()

