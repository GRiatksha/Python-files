from firstwebdjango.InterfaceSegregation.IAdvancedCalculator import IAdvancedCalculator
from firstwebdjango.InterfaceSegregation.IBasicCalculator import IBasicCalculator


class ICalculator(IBasicCalculator, IAdvancedCalculator):
    pass