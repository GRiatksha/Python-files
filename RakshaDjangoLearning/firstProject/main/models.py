from django.db import models

# Create your models here.


class ToDoList(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Items(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    complete = models.BooleanField()

    def __str__(self):
        return self.text



