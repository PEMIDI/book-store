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
        Seller(**result)

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
            'amount' : amount
        }
        Book(**result)


class Customer(User):
    """
     an inheritance from User class, to initiate Costumers in bookstore
    """
    customer_list = []  # all costumers

    def __init__(self, order, *args, **kwargs):
        Customer.customer_list.append(self)
        super().__init__(*args, **kwargs)

    @classmethod
    def sign_up(cls):
        """
        a class method to sign_up Costumer
        """
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
        Seller(**result)
