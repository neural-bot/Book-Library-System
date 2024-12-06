import add_book, delete_book, view_book

def main():
    book_list = []

    print("Welcome to Library System")
    menu = """_____Menu_____
    0. Exit
    1. Add New Book
    2. Delete a Book
    3. View the List of Books
    """
    print(menu)

    option = int(input("Choose a option above: "))

    while True:
        if option < 0 or option > 3:
            print("Enter options from the menu only\n")
        else:
            if option == 0:
                break
            elif option == 1:
                add_book.add_book(book_list)
                break
            elif option == 2:
                isbn_number = input("Enter the ISBN of the book to delete: ")
                delete_book.delete_book(isbn_number)
                break
            elif option == 3:
                view_book.view_book()
                break


if __name__ == "__main__":
    main()