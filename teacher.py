import sqlite3
con = sqlite3.connect('data.db')
c = con.cursor()



def view_profile():  # with name, classes, subject
    pass


def view_all_classes():  # -> select one class -> view students from class and stats -> select one student
    pass


def view_all_students():  # -> select one student
    pass


def view_class_stats():
    pass


def announcement_for_class(class_name, announcement):
    message = input("Enter your message: ").strip()
    c.execute(f"INSERT INTO chat_{class_name} VALUES (?,?)", (self.name, message))
    con.commit()


def get_notifications():
    c.execute(f"SELECT * FROM announcments LIMIT 50")
    history = c.fetchall()
    formatted_data = format_output(history)
    print_formatted_output(formatted_data)


def create_test(teacher_id):
    class_name = f"Class_{input('Enter the name of the class: ').strip().lower()}"
    c.execute("SELECT class_name FROM classes WHERE id IN (SELECT class_id FROM class_enrollment WHERE teacher_id = ?)", (teacher_id,))
    classes = c.fetchall()
    if (class_name,) not in classes:
        print("Invalid class")
        return

    c.execute("SELECT student_id FROM class_enrollment WHERE class_id = (SELECT id FROM classes WHERE class_name = ?)", (class_name,))
    student_ids = c.fetchall()
    student_ids = [item[0] for item in student_ids if item[0] is not None]
    c.execute("SELECT name FROM students WHERE id IN (SELECT student_id FROM class_enrollment WHERE class_id = (SELECT id FROM classes WHERE class_name = ?))", (class_name,))
    student_names = c.fetchall()

    test_name = input("Enter the name of the event: ").strip()
    c.execute(f"INSERT INTO {class_name} (events) VALUES(?)",(test_name,))

    for index, student_name in enumerate(student_names):
        while True:
            try:
                grade = int(input(f"Enter the grade for {student_name[0]}: ").strip())
                if grade < 0 or grade > 100:
                    print("Invalid")
                    continue
                break
            except ValueError:
                print("Invalid grade, not a number!")

        c.execute(f"UPDATE {class_name} SET s{student_ids[index]} = ? WHERE events = ?", (grade, test_name))

    con.commit()


def absence(student_name, reason):
    pass


def suggest(suggestion):
    pass


def format_output(data):
    formatted_data = []
    for name, message in data:
        formatted_name = name.capitalize()
        formatted_message = message.capitalize()
        formatted_data.append((formatted_name, formatted_message))
    return formatted_data


def print_formatted_output(formatted_data):
    for name, message in formatted_data:
        print(f"{name}: {message}")


if __name__ == "__main__":
    create_test(2)
