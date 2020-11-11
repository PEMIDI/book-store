from models.book import Book
import json
from models.finance import Order


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
    seller_lists = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Seller.seller_lists.append(self)

    @classmethod
    def sign_up(cls):
        username = input("Please enter a Username\n")
        password = input("Please enter a Password\n")
        fullname = input("Enter your Fullname\n")
        email = input("Enter your Email\n")
        result = {
            'username': username,
            'password': password,
            'fullname': fullname,
            'email': email
        }
        return Seller(**result)

    @staticmethod
    def add_book(cls):
        """
        static method to add book by seller (Admin)
        """
        name = input("Enter Book name\n")
        author = input("Enter author of book\n")
        price = int(input("enter price of book\n"))
        publish_date = int(input("Enter publish date\n"))
        amount = input("enter amount of book\n")
        result = {
            'name': name,
            'author': author,
            'price': price,
            'publish_date': publish_date,
            'amount': amount
        }
        Book(**result)

    def serialize(self):
        return json.dumps(self)

    @classmethod
    def data(cls):
        """
        a class method returns all sellers data
        """
        return json.dumps([s.__dict__ for s in cls.seller_lists])


class Customer(User):
    """
     an inheritance from User class, to initiate Costumers
    """
    customer_list = []  # all costumers

    def __init__(self, order=Order(), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.order = order
        Customer.customer_list.append(self)

    @staticmethod
    def add_to_order(customer, book_id):
        """
        a method to add book to order.cart
        show means show books, default is None
        """
        for book in Book.book_list:
            if book_id == book.__dict__['book_id']:
                print(book.__dict__)
                customer.order.add_to_cart(**book.__dict__)

        return False

    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    @classmethod
    def sign_in(cls, username, password):
        "a class method to check credential of customer"
        for customer in cls.customer_list:
            verified = username == customer.__dict__['username'] and password == customer.__dict__['password']
            if verified:
                return customer.__dict__
        return False

    @classmethod
    def create(cls, sign_up=None, *args, **kwargs):
        """
        a class method to sign_up Costumer
        """
        if sign_up is not None:
            username = input("Please enter a Username\n")
            password = input("Please enter a Password\n")
            fullname = input("Enter your Fullname\n")
            email = input("Enter your Email\n")
            result = {
                'username': username,
                'password': password,
                'fullname': fullname,
                'email': email
            }
            return Customer(**result)
        return Customer(*args, **kwargs)

    @classmethod
    def check_credentials(cls):
        username = input("enter username\n")
        password = input('enter password\n')
        for customer in Customer.customer_list:
            if customer.__dict__['username'] == username and customer.__dict__['password'] == password:
                return customer

        return None

    @classmethod
    def data(cls):
        """
        a class method returns customer lists in a json type
        """
        return json.dumps([c.__dict__ for c in cls.customer_list], default=lambda o: o.__dict__)
