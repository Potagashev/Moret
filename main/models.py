from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    deadline = models.DateTimeField('deadline')

    def __str__(self):
        return self.name


class Task(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text