from django.db import models
from django_mysql.models import JSONField, Model

class Page(Model):
    name = models.CharField(default="", max_length=255)
    htmltxt = models.TextField(default="")
    jsontxt = JSONField()


    def __str__(self):
        return self.name;
