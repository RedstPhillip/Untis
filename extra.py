from classes import create_school_class
import sqlite3
import string
from math import ceil, floor
con = sqlite3.connect('data.db')
c = con.cursor()


stundentafel: dict = {
    1: {"Math": 4, "English": 3, "Swp": 2},
    2: {"Math": 4, "English": 3, "Swp": 2},
    3: {"Math": 4, "English": 3, "Swp": 2},
    4: {"Math": 4, "English": 3, "Swp": 2},
    5: {"Math": 4, "English": 3, "Swp": 2}
}


def create_classes():
    for level in range(1, 6):
        # students and teachers
        max_students = 3
        c.execute("SELECT id FROM students WHERE school_year = ?", (level,))
        student_ids = [row[0] for row in c.fetchall()]
        classes = distribute_students(student_ids, max_students)
        # subjects
        subjects = list(stundentafel[level].keys())
        letters = string.ascii_lowercase[:len(classes)]
        for school_class, letter in zip(classes, letters):
            name = f"Class_{level}{letter}"
            # aClass_1, Class_1b, Class_1c, Class_2a...
            teachers = distribute_teacher(subjects)
            #print(name)
            result_list = [item[0] for item in teachers]
            #print(f"Teachers:{result_list}")
            #print(f"Classstudents: {school_class}")
            #TODO only execute create_school_class if there are students/teachers
            create_school_class(name, result_list, school_class)


def distribute_teacher(subjects):
    # output: [(2,), (1,), (3,)]
    result = []
    for subject in subjects:
        c.execute("SELECT id FROM teachers WHERE school_subject = ? ORDER BY amount_classes LIMIT 1", (subject,))
        teachers = (c.fetchone())
        result.append(teachers)
        c.execute("UPDATE teachers SET amount_classes = amount_classes + 1 WHERE id = ?", (teachers[0],))
        con.commit()

    return result


def distribute_students(student_ids, max_students):
    if len(student_ids) == 0:
        return []

    amount_students = len(student_ids)
    classes_needed = ceil(amount_students / max_students)
    amount_students_per_class = (amount_students / classes_needed)
    amount_in_first_class = ceil(amount_students_per_class)
    amount_in_other_classes = floor(amount_students_per_class)

    classes = []
    current_class = []
    for student in student_ids:
        if len(classes) == 0:
            if len(current_class) < amount_in_first_class:
                current_class.append(student)
            else:
                classes.append(current_class)
                current_class = [student]
        else:
            if len(current_class) < amount_in_other_classes:
                current_class.append(student)
            else:
                classes.append(current_class)
                current_class = []

    classes.append(current_class)
    return classes



def delete_students_with_school_year_over_5():
    # Query students table for students with school_year over 5
    c.execute("SELECT id, name FROM students WHERE school_year > 5")
    students_to_delete = c.fetchall()

    # Delete each student and their associated parent
    for student_id, student_name in students_to_delete:
        # Call delete_student() function to delete the student and their parent
        del_student_imm(student_name)

    # Commit the transaction
    con.commit()
    print("Deletion of > 5 successful.")


def del_student_imm(student_name):
    c.execute("SELECT id FROM students WHERE name = ?", (student_name,))
    result = c.fetchone()
    if result is not None:
        student_id = result[0]
        c.execute("DELETE FROM students WHERE id = ?", (student_id,))
        c.execute("DELETE FROM parents WHERE child_id = ?", (student_id,))
        con.commit()
        return True
    return False


if __name__ == "__main__":
    create_classes()
