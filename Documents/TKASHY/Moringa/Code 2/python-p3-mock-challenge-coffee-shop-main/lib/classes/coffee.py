from .order import Order  # Import Order class from the appropriate module

class Coffee:
    all_coffees = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Coffee name must be a string")
        if len(name) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        self._name = name
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    def orders(self):
        # Returns a list of all orders associated with this coffee
        return [order for order in Order.all_orders if order.coffee == self]

    def customers(self):
        # Returns a list of unique customers who have ordered this coffee
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        # Returns the total number of orders for this coffee
        return len(self.orders())

    def average_price(self):
        # Calculates and returns the average price of the orders for this coffee
        orders = self.orders()
        if orders:
            return sum(order.price for order in orders) / len(orders)
        return 0
