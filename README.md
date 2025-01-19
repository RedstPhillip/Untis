# School Management System 📚

## Project Overview

This project is a School Management System called Untis and it is designed to manage various aspects of a school, including students, teachers, classes, and grades. The system is built using Python and SQLite for database management. It includes functionalities for administrators, teachers, students, and parents to interact with the system.

## Current Status 🚧

**Note:** This project is currently on pause and is not finished. The prediction functionality is not yet completely implemented, and the existing code may not be of high quality as it was written some time ago. The code is outdated, and would be written differently now. The structure is complete, but the project is on hold.

## Features ✨

### Administrator
- **Create and delete teachers and students**: Administrators can add new teachers and students to the system and remove them when necessary.
- **View classes and teachers**: Administrators can view the list of classes and teachers.
- **Manage school year**: Administrators can start a new school year, which involves promoting students and resetting class enrollments.

### Teacher
- **Create tests and announcements**: Teachers can create tests for their classes and make announcements.
- **View profiles and class stats**: Teachers can view their profiles and statistics for their classes.

### Student
- **Rate teachers and set goals**: Students can rate their teachers and set personal academic goals.
- **Receive messages**: Students can receive messages from class and school chats.

### Parent
- **View child profile and excuse absences**: Parents can view their child's profile and excuse their absences.

## Files and Structure 📂

### `student.py`
Contains functions related to student activities:
- `view_profile()`: Placeholder for viewing student profiles.
- `view_grades_stats()`: Placeholder for viewing grade statistics.
- `receive_message()`: Allows students to receive messages from class or school chats.
- `rate_teacher(student_id)`: Allows students to rate their teachers.
- `set_goal(student_id)`: Allows students to set academic goals.
- `warn_50_percent()`, Placeholder Function that warn students when the grades get critical.
- `suggest()`, Placeholder Function for suggestion to the administrator
- `update_rating(rating, teacher_id)`: Placeholder for correcting teacher ratings.
- `format_output(data)`, `print_formatted_output(formatted_data)`: Helper functions for formatting and printing data.

### `parent.py`
Defines the `Parent` class and its methods:
- `view_child_profile()`: Placeholder for viewing the child's profile.
- `excusing_absences()`: Placeholder for excusing absences.
- `suggest()`, `get_early_warning()`: Placeholder functions for future implementation.

### `main.py`
Main entry point of the application:
- `login(table)`: Handles user login.
- `student_menu(id)`, `teacher_menu(id)`: Display menus for students and teachers.
- `login_menu()`: Displays the login menu.
- `main()`: Calls the `login_menu()` function to start the application.

### `extra.py`
Contains additional functions for managing classes and distributing students and teachers:
- `create_classes()`: Creates classes and assigns students and teachers.
- `distribute_teacher(subjects)`, `distribute_students(student_ids, max_students)`: Helper functions for distributing teachers and students.
- `delete_students_with_school_year_over_5()`, `del_student_imm(student_name)`: Functions for deleting students.

### `designs.py`
Contains functions for displaying menus and other UI elements using the `rich` library:
- `year_calendar(year)`: Generates a calendar for the specified year.
- `student_menu()`, `teacher_menu()`: Display menus for students and teachers.
- `all_teachers_table()`: Displays a table of all teachers.

### `classes.py`
Contains functions for creating and managing school classes:
- `create_school_class(class_name, teachers, students)`: Creates a school class and assigns students and teachers.

### `administrator.py`
Contains functions for administrator activities:
- `view_classes()`, `view_teachers()`, `view_stats()`: Placeholder functions for viewing classes, teachers, and statistics.
- `create_teacher()`, `delete_teacher()`: Functions for creating and deleting teachers.
- `create_student()`, `delete_student()`: Functions for creating and deleting students.
- `announcements()`, `view_suggestions()`: Placeholder functions for announcements and viewing suggestions.
- `new_school_year()`: Resets the school year and reassigns students and teachers.

### `generate_data.py`
Contains functions for generating training data for grade prediction:
- `generate_training_data(num_rows)`: Generates random training data.
- `generate_solution(studied, missing, math_last, math_grades)`: Calculates a predicted grade based on input data.

### `grade_prediction.ipynb`
Jupyter notebook for calculating model inputs and trends for grade prediction:
- `get_inputs(Fach)`: Reads training data and prepares inputs for the model.
- `calculate_trend(grades)`: Calculates the trend of grades using Exponential Weighted Moving Average (EWMA).


### `teacher.py`
Contains functions related to teacher activities:
- `view_profile()`, `view_all_classes()`, `view_all_students()`, `view_class_stats()`: Placeholder functions for viewing profiles, classes, students, and class statistics.
- `announcement_for_class(class_name, announcement)`: Allows teachers to make announcements for a class.
- `get_notifications()`: Retrieves notifications.
- `create_test(teacher_id)`: Allows teachers to create tests for their classes.
- `absence(student_name, reason)`, `suggest(suggestion)`: Placeholder functions for handling absences and suggestions.

### `test.py`
Contains test functions for creating and deleting students and teachers:
- `main()`: Calls functions to delete all data, create students, create teachers, and start a new school year.
- `create_students()`, `create_teachers()`: Functions for creating test students and teachers.
- `del_all()`: Deletes all tables in the database.

## Future Work 🔮

- **Implement prediction functionality**: The grade prediction feature is not yet implemented and needs to be developed.
- **Refactor and improve code quality**: The existing code needs to be refactored and improved for better readability and maintainability.
