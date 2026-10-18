class Student:
    def __init__(self, name, id):
        self.name=name
        self.id=id
        self.__grades=[]

    def get_grades(self):
        return self.__grades

    def add_grades(self, grade):
        return self.__grades.append(grade)    

    def calculate_grades(self):
        return sum(self.__grades)

    def calculate_average(self):
        if len(self.__grades) == 0:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def display_info(self):
        print("Name:", self.name)
        print("ID", self.id)
        print("Grades", self.get_grades())
        print("Total Grades:", self.calculate_grades())
        print("Average Grades:", self.calculate_average())

s1= Student("Ali Ahmed", 2501123)

s1.add_grades(90)
s1.add_grades(80)
s1.add_grades(70)

s1.display_info()





