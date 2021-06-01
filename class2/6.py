class Human:
    def __init__(self, firstname, age, surename, IIN):
        self.firstname = firstname
        self.age = age
        self.surename = surename
        # self.__IIN = IIN

    def eat(self):
        print("Human eating")

    def walk(self):
        print("Human walking")
        # print(self.__IIN)

class Student(Human):
    def __init__(self,firstname, age, surename, gpa, year_of_study, IIN):
        super().__init__(firstname, age, surename, IIN)
        self.gpa = gpa
        self.year_of_study = year_of_study

    def deadline(self):
        print("Student deadline")

    # def show__IIN(self):
        # print(self.IIN)



student1 = Student("Derbes", 18, "Utebaliyev", 3.0, 1)
student1.eat()
student1.deadline()

person1 = Human("Derbes", 18, "Utebaliyev")


