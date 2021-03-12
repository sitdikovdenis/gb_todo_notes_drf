from django.db import models
from uuid import uuid4
from library.models import Author


class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=1024)
    repository_url = models.URLField()
    users = models.ManyToManyField(Author)

    def __str__(self):
        return self.name


class TODO(models.Model):
    CHOICES = (('C', 'Closed'),
               ('A', 'Active'))

    uuid = models.UUIDField(primary_key=True, default=uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='projects')
    text = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')
    state = models.CharField(choices=CHOICES, max_length=7)
