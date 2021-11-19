from django.shortcuts import render
from django.http import HttpResponse
from templates.Person import Person
from django.core.serializers import serialize
import json
import sqlite3


def GetAllEmployees(req):
    connection = sqlite3.connect("persons.db")

    # cursor object
    crsr = connection.cursor()

    persons = crsr.execute("SELECT * FROM Persons").fetchall()
    personsList = []
    for i in persons:
        personsList.append(Person(i[2], i[1]))

    #json_data = serialize("json", personsList, fields=('FirstName', 'LastName'))
    json_data = json.dumps(personsList, default=encoder_func)
    return HttpResponse(json_data, content_type='application/json')


def encoder_func(person):
    return {'FirstName': person.FirstName, 'LastName': person.LastName}



def home(req):
    connection = sqlite3.connect("persons.db")

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


def login(req):
    return render(req, 'login.html')