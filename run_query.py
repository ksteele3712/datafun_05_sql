import sqlite3

conn = sqlite3.connect('project.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS authors (
    author_id TEXT PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL
);
""")

# Insert a sample author
cursor.execute("""
INSERT INTO authors (author_id, first, last)
VALUES ('A001', 'Jane', 'Doe')
""")

cursor.execute("SELECT * FROM authors")
rows = cursor.fetchall()
print(rows)

conn.commit()
conn.close()