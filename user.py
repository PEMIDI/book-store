

class User:
    """
    a class to initiate Base User
    """
    
    def __init__(self, username, password, fullname, email):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
        super.__init__()


class Seller(User):
    """
    to initiate Seller, inheritance from User class
    """

    def __init__(self, *args, **kwargs):
        self.__has_access = False
        super.__init__(*args, **kwargs)

    def has_access(self):
        return self.__has_access
