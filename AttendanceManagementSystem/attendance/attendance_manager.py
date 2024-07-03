from .student import Student
from .attendance_record import AttendanceRecord

class AttendanceManager:
    def __init__(self):
        self.students = []
        self.attendance_record = AttendanceRecord()

    def add_student(self, student_id, name):
        self.students.append(Student(student_id, name))

    def mark_attendance(self, student_id, is_present):
        self.attendance_record.mark_attendance(student_id, is_present)

    def display_attendance(self):
        for student in self.students:
            is_present = self.attendance_record.get_attendance(student.get_id())
            print(f"Student: {student.get_name()} - Present: {is_present if is_present is not None else 'No record'}")
