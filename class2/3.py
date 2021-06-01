class Human:
    def __init__(self, firstname, age, surename):
        self.firstname = firstname
        self.age = age
        self.surename = surename


class Student(Human):
    def __init__(self,firstname, age, surename, gpa, year_of_study):
        super().__init__(firstname, age, surename)
        self.gpa = gpa
        self.year_of_study = year_of_study

student1 = Student("Derbes", 18, "Utebaliyev", 3.0, 1)


