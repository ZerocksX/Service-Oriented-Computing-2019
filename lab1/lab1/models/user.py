from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=500)

    @property
    def get_url(self):
        return "http://127.0.0.1:8000/users/%s" % (self.id,)
