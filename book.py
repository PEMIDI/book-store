
class Book:
    """
    a class to initiate books
    """
    book_list = []

    def __init__(self, name, author, price, year_published, amount):
        self.name = name
        self.author = author
        self.price = price
        self.publish_date = year_published
        self.amount = amount
        Book.book_list.append(self)

    def __str__(self):
        return self.name

    @classmethod
    def search(cls, book_name):
        for book in cls.book_list:
            if book.name == book_name:
                return True
        return False
