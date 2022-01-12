from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    parent_project = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    text = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.text
