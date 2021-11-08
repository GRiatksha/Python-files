class Cricketer:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("my name is",  self.name)


class Bowler(Cricketer):
    def __init__(self):
        super().__init__("max")

    def skill(self):
        print("bowling")


class Batsman(Cricketer):
    def __init__(self):
        super().__init__("ron")

    def skill(self):
        print("batting")


class AllRounder(Bowler, Batsman):
    def __init__(self):
        super().__init__()

    def skill(self):
        Bowler.skill(self)
        Batsman.skill(self)
        print("fielding, wicket keeping")


# bo = Bowler()
# bo.show()
# bo.skill()
# ba = Batsman()
# ba.show()
# ba.skill()
a = AllRounder()
a.show()
a.skill()








