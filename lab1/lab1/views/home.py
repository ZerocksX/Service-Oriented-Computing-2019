from django.http import HttpResponse
from django.shortcuts import render, redirect

from lab1.views import login


def docs(request):
    if not request.user.is_authenticated:
        return redirect(login.login_view)
    return render(request, 'docs.html')
