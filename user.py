from book import Book
import json
from finance import Order


class User:
    """
    a class to initiate Base User
    """
    def __init__(self, username, password, fullname, email):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email

    def add_book(*args, **kwargs):
        """
        add book to book_list via Seller
        """
        Book(*args, **kwargs)


class Seller(User):
    """
    to initiate Seller, inheritance from User class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__has_access = False

    def has_access(self):
        return self.__has_access

    def serialize(self):
        return json.dumps(self)


class Customer(User):
    """
     an inheritance from User class, to initiate Costumers
    """
    customer_list = []  # all costumers

    def __init__(self, order=Order(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order = order
        Customer.customer_list.append(self)

    def add_to_order(self, book):
        book = book.__dict__
        cart = {
            'name': book['name'], 'price': book['price']
        }
        self.order.add_to_cart(**cart)

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__)
