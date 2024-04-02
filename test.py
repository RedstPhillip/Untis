import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()


def main():
    del_all()
    create_students()
    create_teachers()
    pass


def create_students():
    students = ("Raphael", "Phillip", "Paul", "Jonathan")
    parents = ("Mühlbacher", "Lutz", "Wallner", "Laucher")

    for i in range(0, len(students)):
        c.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, birth_year INTEGER, school_year INTEGER, class TEXT, password TEXT, parent_id INTEGER, FOREIGN KEY(parent_id) REFERENCES parents(id))")
        c.execute( "CREATE TABLE IF NOT EXISTS parents(id INTEGER PRIMARY KEY, name TEXT, child_id INTEGER, password TEXT, FOREIGN KEY(child_id) REFERENCES students(id))")
        c.execute("INSERT INTO students (name, birth_year, school_year, class) VALUES (?, ?, ?, ?)", (students[i], 2008, 0, None))
        student_id = c.lastrowid
        c.execute("INSERT INTO parents (name, child_id) VALUES (?, ?)", (parents[i], student_id,))
        parent_id = c.lastrowid
        c.execute("UPDATE students SET parent_id = ? WHERE id = ?", (parent_id, student_id))
        conn.commit()
    print("Students added successfully")


def create_teachers():
    teachers = ["Jungl", "Abart", "Holzmann", "Mayr"]
    subjects = ["English", "Math", "Swp", "English"]
    for i in range(4):
        c.execute(f"CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY, name TEXT, school_subject TEXT, rating INTEGER, password TEXT, amount_classes INTEGER)")
        c.execute(f"INSERT INTO teachers (name, school_subject, amount_classes) VALUES (?,?,?)",(teachers[i], subjects[i],0))
        conn.commit()
    print("Teachers added successfully")


def del_all():
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    for table in tables:
        table_name = table[0]
        c.execute(f"DROP TABLE IF EXISTS {table_name};")
        print(f"Dropped table: {table_name}")
    conn.commit()

if __name__ == '__main__':
    main()
