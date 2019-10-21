from django.contrib import admin

from lab1.models.user import User
from lab1.models.photo import Photo

admin.site.register(User)
admin.site.register(Photo)
