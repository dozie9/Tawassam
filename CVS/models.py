from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Set(models.Model):
    name = models.CharField(max_length=200)
    slide = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name


class Images(models.Model):
    set = models.ForeignKey(
    'Set',
    on_delete=models.CASCADE,
)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.set.name + " image"
