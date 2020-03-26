from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def home_page(request):
    context = {
        "title": "Home page",
        "content": "This will be the content",
    }
    if request.user.is_authenticated:
        context["login"] = "Logged in content"
    return render(request, "home_page.html", context)


def about(request):
    return render(request, 'about_page.html', {'title': 'About'})






