from models.book import Book
from models.user import Customer


def sign_up_or_in():
    choice = input("select one:\n 1-Sign-up\n 2-Sign-in\n")

    if choice == '1':
        online_customer = Customer.create(sign_up=True)
        customer_dashboard(online_customer)

    if choice == '2':
        authed_user = Customer.check_credentials()
        if authed_user is not False:
            print(f"welcome back")
            online_customer = Customer.create(**authed_user.__dict__)
            customer_dashboard(online_customer)
        else:
            print('username or password is wrong!')
            sign_up_or_in()


def customer_dashboard(online_customer):
    sign_in = True
    while sign_in:
        for i, item in enumerate(online_customer.order.cart, start=1):
            print(f"#{i} = {item['name']} with {item['price']}$")


        choice = input('1- show books and buy\n2- sign-out\n \n')

        all_books = Book.show_books()

        if choice == '1':
            print('touched')
            for book in all_books:
                print(f"{book.__dict__['name']}"
                      f" price {book.__dict__['price']}"
                      f" id = {book.__dict__['book_id']} ")

            book_id = input('enter book id to add to your cart\n')
            Customer.add_to_order(online_customer=online_customer, book_id=book_id)
            print(online_customer.order.show_cart())


        if choice == '2':
            sign_up_or_in()

        if choice == '0':
            sign_in = False

    # selected_book = input('enter book name to add to cart')
    # online_customer.order.add_to_order(selected_book)
    # print(f"total = {online_customer.bill()}")
    # dashboard(online_customer)