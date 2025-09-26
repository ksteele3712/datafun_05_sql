
import sqlite3

def apply_db_features():
	conn = sqlite3.connect('project.db')
	cursor = conn.cursor()

	# --- DELETE OPERATIONS ---
	# Delete authors by last name
	cursor.execute("DELETE FROM authors WHERE last IN ('Orwell', 'Austen', 'Bradbury')")

	# Delete authors with a specific first name
	cursor.execute("DELETE FROM authors WHERE first = 'Jane'")

	# Delete books by title
	cursor.execute("DELETE FROM books WHERE title IN ('1984', 'Pride and Prejudice', 'Fahrenheit 451')")

	# Delete books published before a certain year
	cursor.execute("DELETE FROM books WHERE year_published < 1950")

	# Delete books by a specific author
	cursor.execute("DELETE FROM books WHERE author_id = 'A001'")

	# --- UPDATE OPERATIONS ---
	# Update the genre of a book
	cursor.execute("UPDATE books SET genre = 'Science Fiction' WHERE title = '1984'")

	# Correct the year published for a book
	cursor.execute("UPDATE books SET year_published = 1949 WHERE title = '1984'")

	# Update the last name of an author
	cursor.execute("UPDATE authors SET last = 'Rowling' WHERE first = 'J.K.' AND last = 'Rolling'")

	# Change the first name of an author by author_id
	cursor.execute("UPDATE authors SET first = 'George' WHERE author_id = 'A002'")

	conn.commit()
	conn.close()

if __name__ == "__main__":
	apply_db_features()