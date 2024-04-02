import sqlite3
con = sqlite3.connect('data.db')
c = con.cursor()


class Teacher:
    def __init__(self, name: str, school_subject: str, classes: list[SchoolClass], rating: int):
        self.name = name
        self.school_subject = school_subject
        self.classes = classes
        self.rating = rating

    def view_profile(self):  # with name, classes, subject
        pass

    def view_all_classes(self):  # -> select one class -> view students from class and stats -> select one student
        pass

    def view_all_students(self):  # -> select one student
        pass

    def view_class_stats(self):
        pass

    def announcement_for_class(self, class_name, announcement):
        message = input("Enter your message: ").strip()
        c.execute(f"INSERT INTO chat_{class_name} VALUES (?,?)", (self.name, message))
        con.commit()

    def get_notifications(self):
        c.execute(f"SELECT * FROM announcments LIMIT 50")
        history = c.fetchall()
        formatted_data = format_output(history)
        print_formatted_output(formatted_data)

    def chat_with_student(self, student_name, message):
        pass

    def create_test(self, class_name, test_details):
        pass

    def absence(self, student_name, reason):
        pass

    def suggest(self, suggestion):
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
    pass