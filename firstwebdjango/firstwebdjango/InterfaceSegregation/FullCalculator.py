from firstwebdjango.InterfaceSegregation.AdvancedCalculator import AdvancedCalculator
from firstwebdjango.InterfaceSegregation.BasicCalculator import BasicCalculator


class FullCalculator(BasicCalculator, AdvancedCalculator):
    pass