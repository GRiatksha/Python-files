from django.shortcuts import render
import sqlite3


def home(req):
    connection = sqlite3.connect("gfg.db")

    # cursor object
    crsr = connection.cursor()

    # execute the command to fetch all the data from the table emp

#     crsr.execute("""CREATE TABLE Persons (
#     PersonID int,
#     LastName varchar(255),
#     FirstName varchar(255),
#     Address varchar(255),
#     City varchar(255)
# );""")
    crsr.execute("SELECT * FROM Persons")
    crsr.execute("Insert into Persons Values(1,'kumar','anil','add','mys')")
    connection.commit()
    return render(req, 'home.html')