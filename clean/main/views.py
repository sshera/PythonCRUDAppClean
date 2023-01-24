from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import ToDoList, Item

# Create your views here.
def index(response):
    ls = ToDoList.objects.get(name="My List")

    if response.method == "POST":
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False

                item.save()

        elif response.POST.get("add"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("Invalid input")

    return render(response, "main/index.html", {"ls": ls})


def delete_item(request, id):
    ls = ToDoList.objects.get(name="My List")
    item = ls.item_set.get(id=id)
    item.delete()

    return HttpResponseRedirect(reverse("index"))


def update(request, id):
    ls = ToDoList.objects.get(name="My List")
    item = ls.item_set.get(id=id)

    return render(request, "main/edit.html", {"item": item})


def edit(request, id):
    ls = ToDoList.objects.get(name="My List")
    item = ls.item_set.get(id=id)
    txt = request.POST["text"]

    if len(txt) > 2:
        item.text = txt
    else:
        print("Invalid input")

    item.save()

    return HttpResponseRedirect(reverse("index"))
