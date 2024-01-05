from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from .models import *
from .forms import *



def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {
        "title": "Главная страница"
    }
    return render(request, "macroeconomics/index.html", context=context)


def login(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("index")
    else:
        form = LoginUserForm()
    context = {
        "form": form,
        "title": "Логин"
    }
    return render(request, "macroeconomics/login.html", context=context)


def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterUserForm()
    context = {
        "form": form,
        "title": "Регистрация"
    }
    return render(request, "macroeconomics/register.html", context=context)


def macroindex(request, macroindex_slug):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if request.GET:
        name = request.GET.get("name")
        macro_economic_index_id = EconomicIndex.objects.get(slug=name).id
        tables = Table.objects.filter(macro_economic_index__id=macro_economic_index_id)
        economic_index = EconomicIndex.objects.get(id=macro_economic_index_id)
        context = {
            "tables": tables,
            "economic_index": economic_index,
            "title": "Таблица"
        }
        return render(request, "macroeconomics/economic_index.html", context=context)
    
    topic_id = Topic.objects.get(slug=macroindex_slug).id
    economic_indices = EconomicIndex.objects.filter(macro_topic_id=topic_id)
    topics = Topic.objects.all()
    context = {
        "topics": topics,
        "economic_indices": economic_indices,
        "title": "Макроэкономика"
    }
    return render(request, "macroeconomics/macroindex.html", context=context)


def main_macroindex(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    topics = Topic.objects.all()
    context = {
        "topics": topics,
        "title": "Макроэкономика"
    }
    return render(request, "macroeconomics/macroindex.html", context=context)


def logout_user(request):
    logout(request)
    return redirect("index")