from rest_framework import serializers
from templates.Person import Person


class PersonSerializer(serializers.Serializer):
    class Meta:
        model = Person
        fields = ['FirstName', 'LastName']