class Male:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} is running")

    def call(self, contactName):
        print("go to contacts")
        print(f"select {contactName} from the contacts")
        print(f"dialling ..... {contactName}......")

