import sqlite3
connection = sqlite3.connect('student.db')
cursor= connection.cursor()
cursor.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, subject INT, age INT, grade REAL)")
cursor.execute("INSERT INTO students (id,name,subject,age,grade) VALUES (01,'CHAKRI','Business',23,85.5)")
cursor.execute("INSERT INTO students (id,name,subject,age,grade) VALUES (02,'ALEX','DMT',24,90.3)")
cursor.execute("INSERT INTO students (id,name,subject,age,grade) VALUES (03,'MAX','ADSD',25,95.3)")
cursor.execute("SELECT * FROM students")
rows= cursor.fetchall()
for row in rows:
  print (row)
try:
    cursor.execute("SELECT * FROM non_existing_table")
except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")
cursor.execute("INSERT INTO students (name,id,subject,grade) VALUES (?, ?, ?, ?)", ('Bob', 101, 'Pod', 92.3))
connection.commit()
connection.close()
