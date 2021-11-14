from firstwebdjango.InterfaceSegregation.AdvancedCalculator import AdvancedCalculator
from firstwebdjango.InterfaceSegregation.ICalculator import ICalculator
from firstwebdjango.InterfaceSegregation.FullCalculator import RakshaCalculator

# cal = ICalculator()

cal = AdvancedCalculator()

print(cal.Mul(2, 3))

print(cal.Div(2, 3))

