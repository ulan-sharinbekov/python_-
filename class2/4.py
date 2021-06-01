class Human:
    def __init__(self, firstname, age, surename):
        self.firstname = firstname
        self.age = age
        self.surename = surename

    def eat(self):
        print("Human eating")

    def walk(self):
        print("Human walking")

class Student(Human):
    def __init__(self,firstname, age, surename, gpa, year_of_study):
        super().__init__(firstname, age, surename)
        self.gpa = gpa
        self.year_of_study = year_of_study

    def deadline(self):
        print("Student deadline")

class Student2(Student):
    def __init__(self,firstname, age, surename, gpa, year_of_study, temp, width):
        super().__init__(firstname, age, surename, gpa, year_of_study)
        self.temp = temp
        self.width = width


student1 = Student("Derbes", 18, "Utebaliyev", 3.0, 1)
student1.eat()
student1.deadline()

person1 = Human("Derbes", 18, "Utebaliyev")

student2 = Student2("Derbes", 18, "Utebaliyev", 3.0, 1, 36, 50)


