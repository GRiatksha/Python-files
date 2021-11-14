from firstwebdjango.DependencyInversionPrinciple.DatabaseLayer import DatabaseLayer


class BusinessLayer:
    def PerformBusinessOperation(self, id, na):
        databaseObj = DatabaseLayer()
        name = databaseObj.PerformDatabaseOperation(id, )
        print("performing business operation and got ", name)
        return name