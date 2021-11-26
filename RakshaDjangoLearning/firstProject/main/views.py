from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CreateNewList
from .models import ToDoList, Items


def home(response):
    return render(response, "main/home.html", {})


def createToDolist(request):
    form = CreateNewList(request.POST)
    # print(form.errors)
    # form.add_error('name', "max length not")
    # print(type(form.errors))

    if form.is_valid():
        n = form.cleaned_data["name"]
        t = ToDoList(name=n)
        t.save()
        return HttpResponseRedirect('/getToDoListId/%i' % t.id)
    else:
        return render(request, "main/create.html", {"form": form})


def create(response):
    if response.method == "POST":
       form = CreateNewList(response.POST)

       if form.is_valid():
           n = form.cleaned_data["name"]
           t = ToDoList(name=n)
           t.save()

           return HttpResponseRedirect("/getToDoListId/%i" %t.id)

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})


def products(request):
    return HttpResponse("Products page")


def index1(response, id):
    ls = ToDoList.objects.get(id=id)
    print(ls)
    return render(response, "main/list.html", {"ls": ls})


def index2(request, id):
    ls1 = ToDoList.objects.get(id=id)
    return HttpResponse("<h1>%s</h1>" %ls1.name)





# Create your views here.
