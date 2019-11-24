from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from lab1.views import home


def login_view(request):
    if request.method == "GET":
        return render(request, "login/login_form.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home.docs)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)


def logout_view(request):
    logout(request)
    return redirect(login_view)
