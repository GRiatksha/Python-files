from Mobile import Mobile


class Male(Mobile):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"{self.name} is running")

