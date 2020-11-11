from datetime import datetime
import json
import dictfier


class Order:
    """
    a class to initiate customer order
    """

    def __init__(self, cart=[], paid=False):
        # self.date = datetime.now()
        self.paid = paid
        self.cart = cart

    def add_to_cart(self, name, price):
        book = {'name': name, 'price': price}
        self.cart.append(book)

    def show_cart(self):
        for i, item in enumerate(self.cart, start=1):
            print(f"#{i} = {item['name']} with {item['price']}$")

    def bill(self):
        result = 0
        for item in self.cart:
            result += item['price']
        return result

    def serialize(self):
        result = {
            'cart': self.cart,
            'paid': self.paid,
        }
        return json.dumps(result)


