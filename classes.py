class Gender:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show(self):
        print(f"My gender is {self.gender}")

class Male(Gender):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.myownProp = "my Own"

    def show(self):
        print(f"My gender in dervied class {self.gender}")

    def attribute(self):
        print("Male")

class Female(Gender):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def character(self):
        print("Female")

g = Gender("Test",222,"Male")
print(type(g))
m = Male("Rahul", 20, "male")
g = m
print(type(g))
print(g.myownProp)
f = Female("Radha", 20, "female")
g.show()
f.show()
