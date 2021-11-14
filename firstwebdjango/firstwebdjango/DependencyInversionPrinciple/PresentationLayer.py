from firstwebdjango.DependencyInversionPrinciple.BusinessLayer import BusinessLayer


class View:
    def __init__(self, businessLayer):
        self.businessLayer = businessLayer


    def PresentBeautifulView(self, id):
        name = self.businessLayer.PerformBusinessOperation(id)
        print("this is the view of ", name)
        return name




class IBusinessLayer:
    def PerformBusinessOperation(self, id):
        pass