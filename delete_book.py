import csv

def delete_book(isbn_to_delete):
    rows_to_keep = []

    with open("book.csv", "r") as b:
        reader = csv.DictReader(b)

        for row in reader:
            if row["isbn"].strip() != isbn_to_delete.strip():
                rows_to_keep.append(row)
                

    with open("book.csv", "w", newline="") as b:
        writer = csv.DictWriter(b, fieldnames=["title", "author", "isbn", "year", "price"])
        writer.writeheader()

        for row in rows_to_keep:
            writer.writerow(row)