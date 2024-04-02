import sqlite3
con = sqlite3.connect('data.db')
c = con.cursor()

c.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, birth_year INTEGER, school_year INTEGER, class TEXT)")
c.execute("INSERT INTO students (name, birth_year, school_year, class) VALUES (?, ?, ?, ?)", ('Phillip', 2008, 0, None))
con.commit()

c.execute("SELECT * FROM students")
results = c.fetchall()
print(results)

