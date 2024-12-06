import csv
import os

def add_book(book_data):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book 978- ")
    year = int(input("Enter the publish year of the book: "))
    price = input("Enter the price of the book $ ")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price
    }

    file_exists = os.path.isfile("book.csv")
    book_data.append(book)

    with open("book.csv", "a", newline = "") as b:
        writer = csv.DictWriter(b, fieldnames=["title", "author", "isbn", "year", "price"])

        if not file_exists:
            writer.writeheader()

        for book in book_data:
            writer.writerow(book)

