from coffee_shop.customer import Customer
from coffee_shop.coffee import Coffee

class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be an instance of Customer")
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be an instance of Coffee")
        if not isinstance(price, (float, int)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0")
        
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order.all_orders.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee
