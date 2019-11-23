from django.forms import models

from lab1.models.photo import Photo


class PhotoForm(models.ModelForm):
    class Meta:
        model = Photo
        fields = ('title', 'image')
