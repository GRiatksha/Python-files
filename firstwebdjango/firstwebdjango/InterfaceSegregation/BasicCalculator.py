from firstwebdjango.InterfaceSegregation.IBasicCalculator import IBasicCalculator


class BasicCalculator(IBasicCalculator):
    def Add(self, a, b):
        return a + b

    def Sub(self, a, b):
        return a - b

