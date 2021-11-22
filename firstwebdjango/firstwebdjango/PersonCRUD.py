from rest_framework import generics
from templates.Person import Person
import sqlite3
from .serializers import PersonSerializer


class PersonCrud(generics.ListAPIView):
    connection = sqlite3.connect("persons.db")

    # cursor object
    crsr = connection.cursor()

    persons = crsr.execute("SELECT * FROM Persons").fetchall()
    personsList = []
    for i in persons:
        personsList.append(Person(i[2], i[1]))

    # json_data = serialize("json", personsList, fields=('FirstName', 'LastName'))
    queryset = personsList
    serializer_class = PersonSerializer
