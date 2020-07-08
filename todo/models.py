from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    memo = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    finished_datetime = models.DateTimeField(null=True , blank=True)
    important = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title