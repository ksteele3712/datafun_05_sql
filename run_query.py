import sqlite3

conn = sqlite3.connect('project.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM authors")
rows = cursor.fetchall()

# Print table headers
print("author_id | first | last")
print("-" * 30)

# Print each row
for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]}")

conn.close()