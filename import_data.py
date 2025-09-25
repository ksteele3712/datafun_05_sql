import pandas as pd
import sqlite3
import pathlib

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files and insert into database tables."""
    db_file = "project.db"
    author_data_path = pathlib.Path("data", "authors.csv")
    book_data_path = pathlib.Path("data", "books.csv")
    try:
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully from CSV files.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

if __name__ == "__main__":
    insert_data_from_csv()
