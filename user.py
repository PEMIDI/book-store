from book import Book


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


class Customer(User):
    """
     an inheritance from User class, to initiate Costumers in bookstore
    """
    customer_list = []  # all costumers

    def __init__(self, order, *args, **kwargs):
        Customer.customer_list.append(self)
        super().__init__(*args, **kwargs)


