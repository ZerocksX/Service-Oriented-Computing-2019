from django.forms import models

from lab1.models.user import User


class UserForm(models.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
