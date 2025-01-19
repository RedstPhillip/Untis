import sqlite3
con = sqlite3.connect('data.db')
c = con.cursor()


def view_profile():  # name, class, school_year, absence, parent, grades, goal
    pass


def view_grades_stats():  # precise visualization of stats
    pass


def receive_message(student_id):
    option = input("What would you like to open. Class chat (class) or school chat (school): ")
    if option == "class":
        c.execute("SELECT class_name FROM classes WHERE id = (SELECT class_id FROM class_enrollment WHERE student_id = ?)", (student_id,))
        school_class = c.fetchone()[0]
        c.execute(f"SELECT * FROM chat_{school_class} LIMIT 50")
        history = c.fetchall()
        formatted_data = format_output(history)
        print_formatted_output(formatted_data)
    elif option == "school":
        c.execute(f"SELECT * FROM announcments LIMIT 50")




def rate_teacher(student_id):
    c.execute('''CREATE TABLE IF NOT EXISTS ratings (
            id INTEGER PRIMARY KEY,
            rating INTEGER,
            reason TEXT,
            student_id INTEGER,
            teacher_id INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(id),
            FOREIGN KEY(teacher_id) REFERENCES teachers(id)
            )''')
    print("Choose a teacher you want to rate:")
    c.execute("SELECT name FROM teachers WHERE id IN (SELECT teacher_id FROM class_enrollment WHERE class_id = (SELECT class_id FROM class_enrollment WHERE student_id = ?))", (student_id,))
    teachers = c.fetchall()
    for teacher in teachers:
        print(teacher[0])
    selection = input().lower().strip().title()
    teacher_names = [teacher[0] for teacher in teachers]
    if selection in teacher_names:
        c.execute("SELECT id FROM teachers WHERE name = ?", (selection,))
        teacher_id = c.fetchone()[0]
        while True:
            rating = input("Enter a number between 1 and 10: ")
            try:
                rating = int(rating)
            except ValueError:
                print("[bold red]This is not a number!")
                continue
            if rating < 1 or rating > 10:
                continue
            reason = input("Enter a reason: ")
            c.execute("INSERT INTO ratings (rating, reason, student_id, teacher_id) VALUES (?,?,?,?)", (rating, reason, student_id, teacher_id))
            update_rating(rating, student_id)
            break
        print("Rating successful")
        con.commit()
    else:
        print("[bold red]Invalid teacher")


def set_goal(student_id):
    goal = input("Enter your goal for your grades: ")
    if 0 > int(goal) > 100:
        print("[bold red]Invalid, please enter a number between 0 and 100!")
        return

    c.execute("UPDATE students SET goal = ? WHERE id = ?", (goal, student_id))
    con.commit()


def warn_50_percent():
    pass


def suggest():
    pass


def update_rating(rating, teacher_id):
    c.execute("SELECT rating, amount_ratings FROM teachers WHERE id = ?", (teacher_id,))
    teacher_info = c.fetchone()
    if teacher_info is not None:
        curr_rating, amount_ratings = teacher_info
        rating = (curr_rating * amount_ratings + rating) / (amount_ratings + 1)
        c.execute("UPDATE teachers SET rating = ?, amount_ratings = ? WHERE id = ?",
                  (rating, amount_ratings + 1, teacher_id))

    con.commit()


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
    rate_teacher(1)