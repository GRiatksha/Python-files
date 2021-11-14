from Employee import Employee


class DatabaseLayer:
    def PerformDatabaseOperation(self, id, name):
        e = Employee("xyz", 22, 1234)
        print("get rows from database")
        print("return database rows ", e.name)
        return e.name

