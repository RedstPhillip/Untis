import sqlite3
con = sqlite3.connect('data.db')
c = con.cursor()


def create_school_class(class_name: str, teachers: list, students: list):  # list of id
    # Create the classes table if it doesn't exist
    c.execute(f"CREATE TABLE IF NOT EXISTS chat_{class_name} (name text, message text)")
    c.execute("CREATE TABLE IF NOT EXISTS classes (id INTEGER PRIMARY KEY,class_name TEXT)")

    # Insert the class into the classes table
    c.execute("INSERT INTO classes (class_name) VALUES (?)", (class_name,))
    class_id = c.lastrowid  # get class_id


    c.execute('''CREATE TABLE IF NOT EXISTS class_enrollment (
                        class_id INTEGER,
                        student_id INTEGER,
                        teacher_id INTEGER,
                        FOREIGN KEY (class_id) REFERENCES classes(id),
                        FOREIGN KEY (student_id) REFERENCES students(id),
                        FOREIGN KEY (teacher_id) REFERENCES teachers(id),
                        PRIMARY KEY (class_id, student_id)
                    )''')

    # Insert student and teacher IDs into the class_enrollment table
    for student_id in students:
        c.execute('''INSERT INTO class_enrollment (class_id, student_id) VALUES (?, ?)''', (class_id, student_id))

    for teacher_id in teachers:
        c.execute('''INSERT INTO class_enrollment (class_id, teacher_id) VALUES (?, ?)''', (class_id, teacher_id))

    create_table_sql = f"CREATE TABLE IF NOT EXISTS {class_name} (id INTEGER PRIMARY KEY,events TEXT, {', '.join(['s' + str(student_id) + ' INTEGER' for student_id in students])})"
    c.execute(create_table_sql)
    con.commit()


if __name__ == '__main__':
    pass

