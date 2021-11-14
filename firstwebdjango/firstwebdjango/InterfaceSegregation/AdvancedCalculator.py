from firstwebdjango.InterfaceSegregation.IAdvancedCalculator import IAdvancedCalculator


class AdvancedCalculator(IAdvancedCalculator):
    def Mul(self, a, b):
        return a * b

    def Div(self, a, b):
        return a / b
