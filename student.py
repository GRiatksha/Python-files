class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.testid = None
        self.ttt = None

    def get_grade(self):
        print(self.ttt)
        print(self.grade)

class course(student):
    def __init__(self, name, age, grade, namec, max_students ):
        super().__init__(name, age, grade)
        self.namec = namec
        self.max_students = max_students
        self.Students = []

    def add_students(self, students):
        if len(self.Students) < self.max_students:
            self.Students.append(students)
            return True
        return False

    '''def display_std_name(self):
        n = len(self.Students)
        print(n)
        for i in range(n):
            print(self.Students[i].name)'''

    def getStudentNames(self):
        names = []
        n = len(self.Students)
        for stud in self.Students:
            names.append(stud.name)
        return names

    def getStudentNamesByAge(self,age):
        names = []
        n = len(self.Students)
        for i in range(n):
            if self.Students[i].age == age:
                names.append(self.Students[i].name)
        return names








