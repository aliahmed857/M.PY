
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grades = []

    def get_grades(self):
        return self.__grades

    def add_grades(self, grade):
        self.__grades.append(grade)

    def calculate_grade(self):
        return sum(self.__grades)

    def calculate_average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def display_info(self):
        print("Name:", self.name)
        print("ID:", self.student_id)
        print("Grades:", self.get_grades())
        print("Total Grade:", self.calculate_grade())
        print("Average Grade:", self.calculate_average())


student1 = Student("Ahmed", 12345)

student1.add_grades(80)
student1.add_grades(90)
student1.add_grades(70)

student1.display_info()
