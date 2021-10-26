from Mobile import Mobile


class Female(Mobile):
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")