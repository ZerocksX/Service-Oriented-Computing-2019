from django.db.models import F
from django.shortcuts import render

from lab1.models.photo import Photo


def photo_listing(request, user_id):
    """All users"""
    photos = Photo.objects.filter(user_id=user_id)
    return render(request, 'photos/photo_listing.html', {'photos': photos})


def photo_details(request, user_id, photo_id):
    """User details"""
    photo = Photo.objects.filter(id=photo_id).first()
    return render(request, 'photos/photo_details.html', {'photo': photo})
