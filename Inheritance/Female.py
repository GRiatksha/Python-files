class Female:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")

    def call(self, contactName):
        print("go to contacts")
        print(f"select {contactName} from the contacts")
        print(f"dialling ..... {contactName}......")