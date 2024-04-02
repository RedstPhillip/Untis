from student import Student


class Parent:
    def __init__(self, name: str, child: Student):
        self.name = name
        self.child = child

    def view_child_profile(self):
        pass

    def excusing_absences(self):
        pass

    def suggest(self):
        pass

    def get_early_warning(self):
        pass


if __name__ == '__main__':
    pass
