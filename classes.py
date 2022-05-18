
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grades(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def average_grades(self):
        value = 0
        for student in self.students:
            value += student.get_grades()
        return value / len(self.students)

s1 = Student("Bob", 34, 95)
s2 = Student("Joe", 14, 80)
s3 = Student("Karen", 20, 65)

course = Course("Math", 2)
course.add_student(s1)
course.add_student(s2)

print(course.average_grades())