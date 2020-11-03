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


class Costumer(User):
    """
     an inheritance from User class, to initiate Costumers in bookstore
    """
    costumer_list = []  # all costumers

    def __init__(self, *args, **kwargs):
        self.cart = []  # costumer cart
        Costumer.costumer_list.append(self)
        super().__init__(*args, **kwargs)

    def add_to_card(self, book):
        """
        add book to Costumer cart
        """
        self.cart.append(book)

    def show_cart(self):
        """
        show Costumer cart
        """
        return [book for book in self.cart]
