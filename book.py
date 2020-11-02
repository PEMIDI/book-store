

class Book:
    """
    a class to initiate books
    """
    book_list = []

    def __init__(self, name, author, price, publish_date):
        self.name = name
        self.author = author
        self.price = price
        self.publish_date = publish_date
        Book.book_list.append(self)