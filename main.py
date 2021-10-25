class dog:
    def __init__(self, name):
        self.name = name
        print(name)

    def DisplayName(self):
        self.bark()
        print(self.name)

    def bark(self):
        print("bark")

d=dog("timm")
d.DisplayName()

