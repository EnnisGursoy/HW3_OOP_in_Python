class Student:
    def __init__(self, name, student_id, gpa):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa
        self._attendance = 0

    def mark_attendance(self):
        self._attendance += 1

    def get_attendance(self):
        return self._attendance

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"GPA: {self.gpa}")
        print(f"Attendance: {self._attendance}")
        print("-" * 20)

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.addStudents = []

    def addStudent(self, student):
        self.addStudents.append(student)

    def removeStudent(self, student_id):
        self.addStudents = [student for student in self.addStudents if student.student_id != student_id]

    def mark_attendance(self, student_id):
        for student in self.addStudents:
            if student.student_id == student_id:
                student.mark_attendance()
                print(f"Attendance marked for {student.name}.")
                return
        print(f"Student with ID {student_id} not found.")

    def listStudents(self):
        if not self.addStudents:
            print("No students enrolled.")
        else:
            print(f"Students enrolled in {self.course_name}:")
            for student in self.addStudents:
                student.display_info()

student1 = Student("Alice", "S12345", 3.8)
student2 = Student("Bob", "S67890", 3.5)

course = Course("Python Programming")

course.addStudent(student1)
course.addStudent(student2)

print("Students before marking attendance:")
course.listStudents()

course.mark_attendance("S12345")
course.mark_attendance("S67890")
course.mark_attendance("S67890")

print("\nStudents after marking attendance:")
course.listStudents()

course.removeStudent("S12345")

print("\nStudents after removal:")
course.listStudents()
