class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def get_id(self):
        return self.student_id

    def get_name(self):
        return self.name
