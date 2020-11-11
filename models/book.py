import json


class Book:
    """
    a class to initiate books
    """
    book_list = []
    book_id = 1

    def __init__(self, name, author, price, year_published, amount):
        self.name = name
        self.author = author
        self.price = price
        self.publish_date = year_published
        self.amount = amount
        self.book_id = Book.book_id
        Book.book_list.append(self)
        Book.book_id += 1

    def __str__(self):
        return self.name

    @classmethod
    def search(cls, book_name):
        for book in cls.book_list:
            if book.name == book_name:
                return True
        return False

    @classmethod
    def show_books(cls):
        return Book.book_list

    @classmethod
    def data(cls):
        """
        a class method returns book_list data in json type
        """
        return json.dumps([b.__dict__ for b in Book.book_list])

