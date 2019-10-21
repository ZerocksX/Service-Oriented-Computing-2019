from django.db.models import F
from django.shortcuts import render

from lab1.models.user import User


def user_listing(request):
    """All users"""
    users = User.objects.all()
    return render(request, 'users/user_listing.html', {'users': users})


def user_details(request, user_id):
    """User details"""
    user = User.objects.filter(id=user_id).first()
    return render(request, 'users/user_details.html', {'user': user})
