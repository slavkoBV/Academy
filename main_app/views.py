from django.shortcuts import render

from academy_news.models import News
from .models import Contact


def main(request):
    news = News.objects.all()[:2]
    return render(request, 'main/main.html', {'news': news})


def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'main/contacts.html', {'contacts': contacts})
