from rich import print
from rich.prompt import Prompt, Confirm

import sqlite3
con = sqlite3.connect('data.db')
c = con.cursor()


def login(table):
    print("[bold green]You are logging in")
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
    return name


def login_menu() -> str:
    option = Prompt.ask("Log in as:", choices=["Administrator", "Teacher", "Student", "Parent"], default="Student")
    match option:
        case "Administrator":
            pass
        case "Teacher":
            return login("teachers")
        case "Student":
            return login("students")
        case "Parent":
            return login("parents")


def main():
    username = login_menu()


if __name__ == "__main__":
    main()
