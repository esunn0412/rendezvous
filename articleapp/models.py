from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True)

    # user calls it user.article
    # on delete, the articles will become null
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to = 'articles/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
