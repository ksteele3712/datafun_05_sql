
import sqlite3

def apply_db_features():
	conn = sqlite3.connect('project.db')
	cursor = conn.cursor()

	# --- DELETE OPERATIONS EXAMPLES ---
	# Delete authors by last name
	cursor.execute("DELETE FROM authors WHERE last IN ('Orwell', 'Austen', 'Bradbury')")

	# Delete authors with a specific first name
	cursor.execute("DELETE FROM authors WHERE first = 'Jane'")



	# --- UPDATE OPERATIONS EXAMPLES---
	# Update the genre of a book
	cursor.execute("UPDATE books SET genre = 'Science Fiction' WHERE title = '1984'")

	# Update the last name of an author
	cursor.execute("UPDATE authors SET last = 'Rowling' WHERE first = 'J.K.' AND last = 'Rolling'")


	conn.commit()
	conn.close()

if __name__ == "__main__":
	apply_db_features()