from .order import Order  # Ensure the Order class is imported

class Customer:
    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        # Returns a list of orders made by this customer
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        # Returns a list of unique coffees this customer has ordered
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        # Create a new order for this customer
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        # Calculate which customer has spent the most money on a particular coffee
        customer_spending = {}
        for order in Order.all_orders:
            if order.coffee == coffee:
                if order.customer not in customer_spending:
                    customer_spending[order.customer] = 0
                customer_spending[order.customer] += order.price
        if customer_spending:
            # Return the customer who spent the most
            return max(customer_spending, key=customer_spending.get)
        return None
