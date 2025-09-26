import sqlite3
import os

db_path = "project.db"

# List of SQL files to run in order
sql_files = [
    "sql_create/01_drop_tables.sql",
    "sql_create/02_create_tables.sql",
    "sql_create/03_insert_records.sql"
]

def run_sql_file(sql_file_path):
    """Read and execute SQL statements from a file."""
    print(f"Running step: {sql_file_path}")
    if not os.path.exists(sql_file_path):
        print(f"  SQL file not found: {sql_file_path}")
        return
    with open(sql_file_path, 'r') as file:
        sql_script = file.read()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    print(f"  SQL script '{sql_file_path}' executed!\n")

def main():
    for sql_file in sql_files:
        run_sql_file(sql_file)
    print("All steps completed.")

if __name__ == "__main__":
    main()