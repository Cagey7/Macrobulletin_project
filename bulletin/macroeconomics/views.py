from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *


def index(request):
    topics = Topic.objects.all()
    topic_id = Topic.objects.get(name="МАКРОЭКОНОМИКА").pk
    economic_indices = Economic_index.objects.filter(macro_topic_id=topic_id)
    context = {
        "topics": topics,
        "economic_indices": economic_indices,
        "title": "Главная страница"
    }
    return render(request, "macroeconomics/index.html", context=context)


def login(request):
    context = {
        "title": "Логин"
    }
    return render(request, "macroeconomics/login.html", context=context)


def register(request):
    context = {
        "title": "Регистрация"
    }
    return render(request, "macroeconomics/register.html", context=context)


def topic(request, topic_id):
    economic_indices = Economic_index.objects.filter(macro_topic_id=topic_id)
    topics = Topic.objects.all()
    context = {
        "topics": topics,
        "economic_indices": economic_indices,
        "title": "Макроэкономика"
    }
    return render(request, "macroeconomics/topic.html", context=context)


def main_topic(request):
    topics = Topic.objects.all()
    context = {
        "topics": topics,
        "title": "Макроэкономика"
    }
    return render(request, "macroeconomics/topic.html", context=context)


def economic_index(request, economic_index_id):
    tables = Table.objects.filter(macro_economic_index__id=economic_index_id)
    economic_index = Economic_index.objects.get(id=economic_index_id)
    context = {
        "tables": tables,
        "economic_index": economic_index,
        "title": "Регистрация"
    }
    return render(request, "macroeconomics/economic_index.html", context=context)