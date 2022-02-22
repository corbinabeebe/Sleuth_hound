"""
    Contains data models for sleuth_hound.io application
"""
from django.db import models
from django.forms import PasswordInput

# Create your models here.
class User(models.Model):
    """
        User model class that maps objects to users in the user table
    """
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=25, default=None)

class Task(models.Model):
    """
        Task model class that maps objects to task
    """
    TASK_STATUS = (
        ('N', 'New'),
        ('I','In_Progress'),
        ('C','Completed'),
    )
    SEVERITY = (
        ('H', 'High'),
        ('L', 'Low'),
    )
    task_id = models.BigAutoField(primary_key=True)
    project_id = models.ForeignKey('Project', default=None, on_delete=models.CASCADE)
    task_subject = models.CharField(max_length=30)
    details = models.TextField(max_length=500)
    open_date = models.DateTimeField()
    close_date = models.DateTimeField(blank=True)
    task_status = models.CharField(max_length=1, choices=TASK_STATUS)
    severity = models.CharField(max_length=1, choices=SEVERITY)
    assigned_user = models.ForeignKey(
        'User', default=None, on_delete=models.CASCADE)

class Project(models.Model):
    """
        Project model class that maps objects to projects
    """
    project_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()

class Comment(models.Model):
    """
        Comment model class that maps objects to comments in the db
    """
    comment_id = models.BigAutoField(primary_key=True)
    task_id = models.ForeignKey(
        'Task', default=None, on_delete=models.CASCADE)
    body = models.TextField()
