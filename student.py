from parent import Parent

import sqlite3
con = sqlite3.connect('data.db')
c = con.cursor()


class Student:
    def __init__(self, name: str, parent: Parent, school_year=0):
        self.name = name
        self.parent = parent
        self.school_year = school_year

    def view_profile(self):  # name, class, school_year, absence, parent, grades, goal
        pass

    def view_grades_stats(self):  # precise visualization of stats
        pass

    def receive_message(self):
        option = input("What would you like to open. Class chat (class) or school chat (school): ")
        if option == "class":
            c.execute(f"SELECT * FROM chat_{self.school_class} LIMIT 50")
            history = c.fetchall()
            formatted_data = format_output(history)
            print_formatted_output(formatted_data)
        elif option == "school":
            c.execute(f"SELECT * FROM announcments LIMIT 50")
            pass

    def rate_teacher(self):
        pass

    def set_goal(self):
        pass

    def warn_50_percent(self):
        pass

    def suggest(self):
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