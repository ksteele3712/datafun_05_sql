import sqlite3

def run_example_queries():
	conn = sqlite3.connect('project.db')
	cursor = conn.cursor()

	# 1. Count books per author
	print("\nCount books per author:")
	cursor.execute("SELECT author_id, COUNT(*) AS book_count FROM books GROUP BY author_id;")
	for row in cursor.fetchall():
		print(row)

	# 2. Books published after 1950
	print("\nBooks published after 1950:")
	cursor.execute("SELECT title, year_published FROM books WHERE year_published > 1950;")
	for row in cursor.fetchall():
		print(row)

	# 3. Group books by year published
	print("\nGroup books by year published:")
	cursor.execute("SELECT year_published, COUNT(*) AS books_published FROM books GROUP BY year_published;")
	for row in cursor.fetchall():
		print(row)

	# 4. List books with author names
	print("\nList books with author names:")
	cursor.execute("SELECT books.title, authors.first_name, authors.last_name FROM books JOIN authors ON books.author_id = authors.author_id;")
	for row in cursor.fetchall():
		print(row)

	# 5. Sort authors by last name
	print("\nSort authors by last name:")
	cursor.execute("SELECT first_name, last_name FROM authors ORDER BY last_name ASC;")
	for row in cursor.fetchall():
		print(row)

	conn.close()

if __name__ == "__main__":
	run_example_queries()
