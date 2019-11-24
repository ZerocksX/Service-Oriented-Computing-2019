import json

from django.db.models import F
from django.http import QueryDict, HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from lab1.forms.user import UserForm
from lab1.models.user import User


def user_listing(request):
    """/users"""
    if not request.user.is_authenticated:
        return HttpResponse(status=403)
    if request.method == "GET":
        users = User.objects.all()
        return render(request, 'users/user_listing.html', {'users': users})
    elif request.method == "POST":
        t = QueryDict('', mutable=True)
        t.update(json.loads(request.body.decode("utf-8")))
        form = UserForm(t)
        if form.is_valid():
            user = form.save(commit=True)
            response = HttpResponse()
            response['location'] = user.get_url
            response.status_code = 201
            return response
        else:
            return HttpResponse(form, status=400)
    else:
        return HttpResponse(status=405)


def user_details(request, user_id):
    """/users/{id}"""
    if not request.user.is_authenticated:
        return HttpResponse(status=403)
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == "GET":
        return render(request, 'users/user_details.html', {'user': user})
    elif request.method == "DELETE":
        user.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)
