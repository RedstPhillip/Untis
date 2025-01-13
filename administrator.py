import sqlite3
from math import ceil, floor
from extra import del_student_imm, delete_students_with_school_year_over_5, distribute_students, create_classes


con = sqlite3.connect('data.db')
c = con.cursor()


def view_classes():
    pass


def view_teachers():  # type in name -> show teacher-profile -> rating, classes, usw
    pass


def view_stats():  # from all students -> average grades, dropout percentage
    pass


def create_teacher():
    teacher_name: str = input("Enter the name: ").strip().lower().title()
    school_subject: str = input("Enter the school subject: ").strip().lower().title()
    c.execute(f"CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY, name TEXT, school_subject TEXT, rating INTEGER, amount_ratings INTEGER, password TEXT, amount_classes INTEGER)") #TODO at the end: "", FOREIGN KEY(kv) REFERENCES classes(id))""
    c.execute(f"INSERT INTO teachers (name, school_subject,rating, amount_ratings) VALUES (?,?,?,?,?)", (teacher_name, school_subject,0, 0, 0))
    con.commit()


def delete_teacher():
    teacher_name: str = input("Enter the teacher you want to delete: ").strip().lower().title()
    c.execute("SELECT id FROM teachers WHERE name = ?", (teacher_name,))
    result = c.fetchone()
    if result is not None:
        teacher_id = result[0]
        c.execute("DELETE FROM teachers WHERE id = ?", (teacher_id,))
        con.commit()
        print(f"You successfully deleted the Teacher with the name {teacher_name}")


def create_student():
    student_name: str = input("Enter the name: ").strip().lower().title()
    parent: str = input("Enter the parent's name: ").strip().lower().title()
    while True:
        try:
            birth_year: int = int(input("Enter the birth year: ").strip())
            break
        except ValueError:
            print("The birth year is not an integer")

    c.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, birth_year INTEGER, school_year INTEGER, class TEXT, password TEXT, goal INTEGER, parent_id INTEGER, FOREIGN KEY(parent_id) REFERENCES parents(id))")
    c.execute("CREATE TABLE IF NOT EXISTS parents(id INTEGER PRIMARY KEY, name TEXT, child_id INTEGER, password TEXT, FOREIGN KEY(child_id) REFERENCES students(id))")
    c.execute("INSERT INTO students (name, birth_year, school_year, class, goal) VALUES (?, ?, ?, ?, ?)",(student_name, birth_year, 0, None, None))
    student_id = c.lastrowid
    c.execute("INSERT INTO parents (name, child_id) VALUES (?, ?)", (parent, student_id))
    parent_id = c.lastrowid
    c.execute("UPDATE students SET parent_id = ? WHERE id = ?", (parent_id, student_id))
    con.commit()


def delete_student():
    student_name: str = input("Enter the student you want to delete: ").strip().lower().title()
    if del_student_imm(student_name):
        reason = input("Why do you want to delete the student? (left) or (kicked out) or (other)")
        if reason == "left":
            #TODO remark
            pass
        elif reason == "kicked out":
            #TODO remark
            pass
        elif reason == "other":
            #TODO remark
            pass
        print(f"Succesfully deleted {student_name} and his parent.")
    else:
        print(f"Couldn't find {student_name}. Perhaps you have misspelt.")


def announcements():  # to everyone, teachers, teacher, class, students, student, parents
    message = input("Enter message: ")
    c.execute(f"INSERT INTO announcments VALUES (?)", (message))


def view_suggestions():  # from teacher, student, class to administrator, suggestions for improvement
    pass


def new_school_year():
    # delete everything:
    c.execute("DROP TABLE IF EXISTS class_enrollment")
    c.execute("DROP TABLE IF EXISTS classes")
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'Class%'")
    tables = c.fetchall()
    for table in tables:
        class_name = table[0]
        c.execute(f"DROP TABLE IF EXISTS '{class_name}'")
        chat_name = f"chat_{class_name}"
        c.execute(f"DROP TABLE IF EXISTS '{chat_name}'")
    con.commit()
    c.execute("DROP TABLE IF EXISTS announcments")

    c.execute("UPDATE students SET school_year = school_year + 1")
    c.execute("CREATE TABLE IF NOT EXISTS announcments (messages text)")
    con.commit()
    delete_students_with_school_year_over_5()
    create_classes()




if __name__ == "__main__":
    new_school_year()
