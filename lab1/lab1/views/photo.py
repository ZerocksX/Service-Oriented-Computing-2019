from django.core import serializers
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.shortcuts import render

from lab1.forms.photo import PhotoForm
from lab1.models.photo import Photo
from lab1.models.user import User

import json


def photo_details(request, user_id, photo_id):
    try:
        photo = Photo.objects.get(id=photo_id, user_id=user_id)
    except Photo.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == "GET":
        return render(request, 'photos/photo_details.html', {'photo': photo})
    elif request.method == "PUT":
        t = QueryDict('', mutable=True)
        t.update(json.loads(request.body.decode("utf-8")))
        form = PhotoForm(t)
        if form.is_valid():
            updated_photo = form.save(commit=False)
            if updated_photo.title is not None:
                photo.title = updated_photo.title
            if updated_photo.image is not None:
                photo.image = updated_photo.image
            photo.save()
            return HttpResponseRedirect(photo.get_url)
        else:
            return HttpResponse(form, status=400)
    elif request.method == "DELETE":
        photo.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)


def photos_collection(request, user_id):
    if request.method == "POST":
        t = QueryDict('', mutable=True)
        t.update(json.loads(request.body.decode("utf-8")))
        form = PhotoForm(t)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = User.objects.get(id=user_id)
            photo.save()
            response = HttpResponseRedirect(photo.get_url)
            response.status_code = 201
            return response
        else:
            return HttpResponse(form, status=400)
    elif request.method == "GET":
        photos = Photo.objects.filter(user_id=user_id)
        return render(request, 'photos/photo_listing.html', {'photos': photos})
    else:
        return HttpResponse(status=405)
