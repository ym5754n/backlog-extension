from django.db import models

# Create your models here.
class Issue(models.Model):
    summary = models.CharField('件名', max_length=255)
    description = models.TextField('詳細')

    def __str__(self):
        return self.summary