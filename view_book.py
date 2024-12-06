from tabulate import tabulate
import pandas as pd

def view_book():
    table_view = pd.read_csv("book.csv")
    table_view.index += 1

    print(tabulate(table_view, headers="keys", tablefmt="fancy_grid"))