import sqlite3
connection = sqlite3.connect('example.db')
cursor= connection.cursor()
cursor.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, grade REAL)")
cursor.execute("INSERT INTO students (name,grade) VALUES ('ALICE', 85.5)")
cursor.execute("SELECT * FROM students")
rows= cursor.fetchall()
for row in rows:
  print (row)
connection.commit()
try:
    cursor.execute("SELECT * FROM non_existing_table")
except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ('Bob', 92.3))
connection.commit()
connection.close()
