from django.db import models

from lab1.models.user import User


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    image = models.TextField()
    title = models.CharField(max_length=100)

    @property
    def get_url(self):
        return "http://127.0.0.1:8000/users/%s/photos/%s" % (self.user_id, self.id)
