class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def get_name(self):
        return self.name

    def set_gpa(self, n):
        self.gpa = n


student1 = Student("Derbes", 2.5)

print(student1.gpa)
student1.set_gpa(4.0)
print(student1.gpa)
