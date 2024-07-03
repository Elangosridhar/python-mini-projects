class AttendanceRecord:
    def __init__(self):
        self.attendance_map = {}

    def mark_attendance(self, student_id, is_present):
        self.attendance_map[student_id] = is_present

    def get_attendance(self, student_id):
        return self.attendance_map.get(student_id, None)

    def get_all_attendance(self):
        return self.attendance_map
