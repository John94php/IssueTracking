from django.db import models
from django.contrib.auth.models import User
from Projects.models import Project

# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "issue_category"


class Issue(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(Project,on_delete=models.SET_NULL,null=True)
    start_date = models.DateField()
    due_date = models.DateField()
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "issue"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Issue, on_delete=models.CASCADE)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    descriptions = models.TextField()

    def __str__(self):
        return self.descriptions

    class Meta:
        db_table = "issue_comments"
