from firstwebdjango.InterfaceSegregation.ICalculator import ICalculator
from firstwebdjango.InterfaceSegregation.FullCalculator import RakshaCalculator

# cal = ICalculator()

cal = RakshaCalculator()

print(cal.Add(2, 3))

print(cal.Sub(2, 3))
