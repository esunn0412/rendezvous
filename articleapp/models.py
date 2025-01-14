from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    # user 에서 접근하는 이름 user.article
    # on delete, the articles will become null, not entirely gone
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to = 'articles/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
