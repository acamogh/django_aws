from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=10000)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class User(models.Model):
    title=models.ForeignKey(Post)
    user_name=models.CharField('User Name',max_length=30)

    def __str__(self):
        return self.user_name