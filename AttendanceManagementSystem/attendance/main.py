from attendance.attendance_manager import AttendanceManager

def main():
    manager = AttendanceManager()

    while True:
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            manager.add_student(student_id, name)
        elif choice == '2':
            student_id = input("Enter student ID: ")
            is_present = input("Is present (true/false): ").lower() == 'true'
            manager.mark_attendance(student_id, is_present)
        elif choice == '3':
            manager.display_attendance()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
