from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path(r'getToDoListId/<int:id>', views.index1, name='index1'),
    path("getToDoListName/<int:id>", views.index2, name='index2'),
    path("create/", views.create, name='create'),
    path("createToDolist/", views.createToDolist, name='createToDolist'),
]