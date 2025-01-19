from rich import print
from rich.prompt import Prompt, Confirm
from rich.console import Console
import designs
import student

import sqlite3

import teacher

con = sqlite3.connect('data.db')
c = con.cursor()


def login(table):
    while True:
        name = input("Enter your name: ").strip().title()
        password = input("Enter your password: ").strip()

        # check if user in database and retrieve password
        c.execute(f"SELECT password FROM {table} WHERE name = ?", (name,))
        result = c.fetchone()
        if result is None:
            print("[bold red]User does not exist!\n")
            continue

        real_password = result[0]

        if real_password is None:
            while True:
                # student exist but has no password
                confirm = Confirm.ask(f"Your new password is {password}. Is this correct?", default="y")
                if confirm:
                    c.execute(f"UPDATE {table} SET password = ? WHERE name = ?", (password, name))
                    con.commit()
                    print("[bold green]Password set successfully.")
                    # login
                    break
                password = input("Enter your new password: ").strip()
            break
        else:
            if real_password == password:
                # student exist and has password
                # login
                break
            print("[bold red]Incorrect password\n")
            continue

    print(f"[green]Hello {name}! You successfully logged in as {name}\n")

    print(f"Table: {table}")
    name = name.title()
    print(f"Name: {name}")
    c.execute(f"SELECT id FROM {table} WHERE name = ?", (name,))
    user_id = c.fetchone()[0]
    print(f"User_id: {user_id}")
    return user_id


def student_menu(id):
    designs.student_menu()
    option = input("Enter your option: ").strip().lower()

    match option:
        case "1" | "notifications":
            student.receive_message(id)
        case "2" | "grades":
            pass
        case "3" | "absences":
            pass
        case "4" | "rate":
            student.rate_teacher(id)
        case "5" | "goal":
            student.set_goal(id)
        case "6" | "suggest":
            pass
        case "7" | "exit":
            raise SystemExit("Bye!")


def teacher_menu(id):
    designs.teacher_menu()
    option = input("Enter your option: ").strip().lower()

    match option:
        case "1" | "chat":
            pass
        case "2" | "test":
            teacher.create_test(id)
        case "3" | "announcement":
            pass
        case "4" | "grades":
            pass
        case "5" | "absence":
            pass
        case "6" | "suggest":
            pass
        case "7" | "exit":
            raise SystemExit("Bye!")



def login_menu():
    option = Prompt.ask("Log in as:", choices=["Administrator", "Teacher", "Student", "Parent"], default="Student")
    match option:
        case "Administrator":
            pass
        case "Teacher":
            id = login("teachers")
            main_menu = teacher_menu(id)
        case "Student":
            student_id = login("students")
            main_menu = student_menu(student_id)
        case "Parent":
            login("parents")


def main():
    login_menu()


if __name__ == "__main__":
    main()
