from rich.console import Console
from rich.columns import Columns
from rich.layout import Layout
from rich.table import Table, Column
from rich.panel import Panel
from rich.text import Text
from rich import box


from datetime import datetime
import calendar

import sqlite3
con = sqlite3.connect('data.db')
c = con.cursor()


def year_calendar(year):
    current_date = datetime.today()
    today = datetime.today()
    year = int(year)
    cal = calendar.Calendar()
    today_tuple = today.day, today.month, today.year
    current_day, current_month, current_year = current_date.day, current_date.month, current_date.year
    #test_tuple_list = [(24, 4, 2024), (25, 4, 2024), (26, 4, 2024), (28, 4, 2024)]
    test_tuple_list = []

    tables = []

    table = Table(
        # title=f"{calendar.month_name[current_month]} {year}",
        style="green",
        box=box.SIMPLE_HEAVY,
        padding=0,
    )

    for week_day in cal.iterweekdays():
        table.add_column(
            "{:.3}".format(calendar.day_name[week_day]), justify="right"  # first 3 letters of month
        )

    month_days = cal.monthdayscalendar(year, current_month)
    for weekdays in month_days:
        days = []
        for index, day in enumerate(weekdays):
            day_label = Text(str(day or ""), style="magenta")
            if index in (5, 6):
                day_label.stylize("blue")
            if day and (day, current_month, year) == today_tuple:
                day_label.stylize("white on green")
            for test in test_tuple_list:
                if day and (day, current_month, year) == test:
                    day_label.stylize("white on dark_blue")
            days.append(day_label)
        table.add_row(*days)

    # tables.append(Align.center(table))
    tables.append(table)

    console = Console()
    columns = Columns(tables, padding=1, expand=True)
    return table


def student_menu():
    console = Console()
    profile, options = Text(), Text()

    name = "Raphael Mühlbacher"
    school_class = "1BHWII"
    age = "14"
    parent = "Parent Mühlbacher"
    grade = "93%"

    # profile.append(Text(f"{name}", style="bold green"))
    # profile.append(Text(f" -- {school_class}" + "\n \n", style="bold"))
    # profile.append(Text(f"{age} years old \n", style="red"))
    # profile.append(Text(f"{grade} \n", style="bold green"))
    # profile.append(Text(parent, style="bold"))
    profile.append("Placeholder")

    options.append(Text("(1) Notifications\n", style="bold green"))
    options.append(Text("(2) Grades \n", style="bold green"))
    options.append(Text("(3) Absences\n", style="bold green"))
    #options.append(Text("(4) Class Overview \n", style="bold green"))
    #options.append(Text("(5) view Calendar \n", style="bold green"))
    options.append(Text("(4) rate Teacher\n", style="bold green"))
    #options.append(Text("(7) Homework/Exams \n", style="bold green"))
    options.append(Text("(5) set goal\n", style="bold green"))
    options.append(Text("(6) suggest\n", style="bold green"))
    options.append(Text("(7) Exit\n", style="bold red"))


    layout = Layout()
    layout.split_column(
        Layout(name="upper", ratio=1),
        Layout(name="lower", ratio=1)
    )

    layout["upper"].split_row(
        Layout(Panel(profile, title="Profile", padding=(1, 1)), name="uleft", ratio=1),
        Layout(Panel(year_calendar(2024), title="Calendar"), name="uright", ratio=1)
    )
    layout["lower"].split_row(
        Layout(Panel("Placeholder", title="Placeholder", padding=(1, 1)), name="lleft", ratio=1),
        Layout(Panel(options, title="Options", padding=(1, 1)), name="lright", ratio=1)
    )

    console.print(layout, height=22, width=70)


def teacher_menu():
    console = Console()
    profile, options = Text(), Text()

    name = "Raphael Mühlbacher"
    school_class = "1BHWII"
    age = "14"
    parent = "Parent Mühlbacher"
    grade = "93%"

    # profile.append(Text(f"{name}", style="bold green"))
    # profile.append(Text(f" -- {school_class}" + "\n \n", style="bold"))
    # profile.append(Text(f"{age} years old \n", style="red"))
    # profile.append(Text(f"{grade} \n", style="bold green"))
    # profile.append(Text(parent, style="bold"))
    profile.append("Placeholder")

    options.append(Text("(1) chat\n", style="bold green"))
    options.append(Text("(2) create Test \n", style="bold green"))
    options.append(Text("(3) announcement\n", style="bold green"))
    #options.append(Text("(4) Class Overview \n", style="bold green"))
    #options.append(Text("(5) view Calendar \n", style="bold green"))
    options.append(Text("(4) rate Teacher\n", style="bold green"))
    #options.append(Text("(7) Homework/Exams \n", style="bold green"))
    options.append(Text("(5) view grades\n", style="bold green"))
    options.append(Text("(6) suggest\n", style="bold green"))
    options.append(Text("(7) Exit\n", style="bold red"))


    layout = Layout()
    layout.split_column(
        Layout(name="upper", ratio=1),
        Layout(name="lower", ratio=1)
    )

    layout["upper"].split_row(
        Layout(Panel(profile, title="Profile", padding=(1, 1)), name="uleft", ratio=1),
        Layout(Panel(year_calendar(2024), title="Calendar"), name="uright", ratio=1)
    )
    layout["lower"].split_row(
        Layout(Panel("Placeholder", title="Placeholder", padding=(1, 1)), name="lleft", ratio=1),
        Layout(Panel(options, title="Options", padding=(1, 1)), name="lright", ratio=1)
    )

    console.print(layout, height=22, width=70)


def all_teachers_table():
    c.execute("SELECT name, school_subject, rating FROM teachers")
    teachers = c.fetchall()
    print(teachers)

    table = Table(title="Teachers", show_lines=True, box=box.ROUNDED, header_style="bold cyan")
    table.add_column("Name", justify="left",  no_wrap=True)
    table.add_column("Subject", justify="left",  no_wrap=True)
    table.add_column("Rating", justify="left",  no_wrap=True)

    for teacher in teachers:
        if teacher[2] == 0:
            table.add_row(teacher[0], teacher[1], "no rating")
            continue
        table.add_row(teacher[0], teacher[1], str(round(teacher[2], 2)))

    console = Console()
    console.print(table)


if __name__ == "__main__":
    all_teachers_table()
