from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=200,null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'