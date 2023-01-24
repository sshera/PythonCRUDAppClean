from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<int:id>", views.delete_item, name="delete_item"),
    path("update/<int:id>", views.update, name="update"),
    path("update/edit/<int:id>", views.edit, name="edit"),
]
