from django.http import HttpResponse
from django.shortcuts import render


def docs(request):
    if not request.user.is_authenticated:
        return HttpResponse(status=403)
    return render(request, 'docs.html')