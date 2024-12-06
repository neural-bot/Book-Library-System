# Library Management System

This is a **Library Management System** built in Python. It provides a simple command-line interface to **add, view, and delete books**. The system uses **CSV files** for storing book data and displays the book list in a well-formatted table.

---

## Features

- **Add New Book:** Input a book's title, author, ISBN, publish year, and price.
- **Delete Book:** Remove a book by its ISBN number.
- **View Books:** View all books in a tabular format with neatly formatted headers.
- **Persistent Storage:** Book data is saved in a `CSV` file.

---

## Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.x**
2. **tabulate** library  
   Install using:
   ```bash
   pip install tabulate
   ```
3. **pandas** library  
   Install using:
   ```bash
   pip install pandas
   ```

---

## File Structure

```
├── add_book.py          # Function to add a new book to the 
|                           system
|
├── delete_book.py       # Function to delete a book using 
|                           its ISBN
|
├── view_book.py         # Function to view the list of  
|                           books in tabular form
|
├── book.csv             # Stores the list of books (created 
|                           automatically)
|
├── main.py              # Main file to run the program
|
|
└── README.md            # Project documentation
```

---

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/itsnajibul/Library-Management-System.git
   cd library-system
   ```

2. **Run the program:**
   ```bash
   python main.py
   ```

3. **Menu Options:**
   ```
   _____Menu_____
   0. Exit
   1. Add New Book
   2. Delete a Book
   3. View the List of Books
   ```

4. **Usage Flow:**
   - Choose an option from the menu.
   - Add books with their details or delete books by entering their ISBN.
   - View the current book list as needed.

---

## Code Overview

1. **Adding a Book:**  
   The `add_book` function collects book information and stores it in `book.csv`.

2. **Viewing Books:**  
   The `view_book` function reads the CSV file and displays data in a **fancy grid format** using the `tabulate` library.

3. **Deleting a Book:**  
   The `delete_book` function removes a book by matching the ISBN and rewrites the CSV file.

---

## Example Output

**View Books:**

```
╒════╤══════════════════════╤═════════════════╤═════════════╤════════╤══════════╕
│    │ title                │ author          │ isbn        │   year │ price    │
╞════╪══════════════════════╪═════════════════╪═════════════╪════════╪══════════╡
│  1 │ The Alchemist        │ Paulo Coelho    │ 978-1234567 │   1988 │ $10.99   │
│  2 │ To Kill a Mockingbird│ Harper Lee      │ 978-2345678 │   1960 │ $12.50   │
╘════╧══════════════════════╧═════════════════╧═════════════╧════════╧══════════╛
```

---

## Contributions

Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvement.

---

## Author

**MD NAJIB UL AZAM MAHI**

---

Enjoy using the Library Management System! 🚀