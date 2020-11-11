from auth import check_credentials
from dashboard import dashboard
from models.user import Seller, Customer
from models.book import Book

if __name__ == '__main__':
    # ----------------------DATA--------------------------------------
    s1 = Seller('pemidi', '12345', 'peyman rashidi', 'pemidi@zoho.com')
    # --------------------------------------------------------------------------
    book1 = Book(name='book 1', author='newport 1', price=1, year_published=2018, amount=20)
    book2 = Book(name='book 2', author='newport 2', price=10, year_published=2018, amount=20)
    book3 = Book(name='book 3', author='newport 3', price=8, year_published=2018, amount=20)
    book4 = Book(name='book 4', author='newport 4', price=10, year_published=2018, amount=10)
    book5 = Book(name='book 5', author='newport 5', price=100, year_published=2018, amount=20)
    # ------------------------------------------------------------------------------
    c1 = Customer(username='1', password='1',
                  fullname='poya rashidi', email='poya@zoho.com')
    # -------------------------------------------------------------------------------------
    c1.add_to_order(book1)
    c1.add_to_order(book2)


    # ----------------------DATA--------------------------------------------

    def sign_up_or_in():
        choice = input("select one:\n 1-Sign-up\n 2-Sign-in\n")

        if choice == '1':
            online_customer = Customer.create(sign_up=True)
            dashboard(online_customer)

        if choice == '2':
            authed_user = check_credentials()
            if authed_user is not False:
                print(f"welcome back")
                online_customer = Customer.sign_in(**authed_user)
                dashboard(online_customer)
            else:
                print('username or password is wrong!')
                sign_up_or_in()


    # ------------------------------

    # -----------------------------------------------------------

    # ------------------------Start-----------------------

    def run():
        # show sign in / sign -up
        sign_up_or_in()

        # if sign up :
        # create customer

        # elif sign in:
        # check_credentials


    run()
