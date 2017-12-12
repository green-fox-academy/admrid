class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print('Hi, I\'m ' + str(self.name) + ', ' + 'a ' + str(self.age) + ' age year old ' +  str(self.gender) + '.')

    def get_goal(self):
        print('My goal is: Live for the moment!')



class Student(Person):
    def __init__(self, name, age, gender, previous_organization, skipped_days = 0):
        super().__init__(name, age, gender)
        self.prev_org = previous_organization
        self.skipped_days = skipped_days

    def get_goal(self):
        print('Be a junior software developer.')

    def introduce(self):
        print('Hi, I\'m ' + self.name + ', a'  + str(self.age) + ' year old ' +  self.gender + ' from ' + self.prev_org + ' who skipped ' + str(self.skipped_days) + ' days from the course already.')
 #      print("Hi, I'm " + self.name + ", a " + str(self.age) + " year old " + self.gender  + " from " + self.prev_org + " who skipped " + str(self.skipped_days) + ' days from the course already.')

    def skip_days(self, number_of_days):
        self.number_of_days = number_of_days
        self.skipped_days += number_of_days 



class Mentor(Person):
    def __init__(self, name, age, gender, level):
        super().__init__(name, age, gender)
        self.level = level

    def get_goal(self):
        print('Educate brilliant junior software developers.')

    def introduce(self):
        print('Hi, I\'m ' + str(self.name) + ', ' + 'a ' + str(self.age) + ' age year old ' +  str(self.gender) + str(self.level) + ' mentor.')



class Sponsor(Person):
    def __init__(self, name, age, gender, company, hired_students = 0):
        super().__init__(name, age, gender)
        self.company = company
        self.hired_students = hired_students

    def get_goal(self):
        print('Hire brilliant junior software developers.')
    
    def introduce(self):
        print('Hi, I\'m ' + str(self.name) + ', ' + 'a ' + str(self.age) + ' age year old ' +  str(self.gender) + ' who represents ' + str(self.company) + ' and hired ' + str(self.hired_students) + 'students so far.')
    
    def hire(self):
        self.hired_students += 1



class PallidaClass():
    def __init__(self, class_name):
        self.class_name = class_name
        self.students = []
        self.mentors = []

    def add_student(self, Student):
        self.students.append(Student)
    
    def add_mentor(self, Mentor):
        self.mentors.append(Mentor)

    def info(self):
        print('Pallida ' + self.class_name + ' class has ' + str(len(self.students)) + ' students and ' + str(len(self.mentors)) + ' mentors.')
#       print("Pallida " + self.class_name + " class has " + str(len(self.students)) + " students and " + str(len(self.mentors)) + " mentors.")
    


people = []

mark = Person('Mark', 46, 'male')
people.append(mark)
jane = Person('Jane Doe', 30, 'female')
people.append(jane)
john = Student('John Doe', 20, 'male', 'BME')
people.append(john)
studentJane = Student('Jane Doe', 30, 'female', 'The School of Life', 0)
people.append(studentJane)
gandhi = Mentor('Gandhi', 148, 'male', 'senior')
people.append(gandhi)
mentorJane = Mentor('Jane Doe', 30, 'female', 'intermediate')
people.append(mentorJane)
sponsorJane = Sponsor('Jane Doe', 30, 'female', 'Google', 0)
elon = Sponsor('Elon Musk', 46, 'male', 'SpaceX')
people.append(elon)
people.append(sponsorJane)
studentJane.skip_days(3)

for i in range(3):
    elon.hire()

for i in range(5):
    sponsorJane.hire()

for member in people:
    member.introduce()
    member.get_goal()

badass = PallidaClass('BADA55')
badass.add_student(studentJane)
badass.add_student(john)
badass.add_mentor(mentorJane)
badass.add_mentor(gandhi)
badass.info()