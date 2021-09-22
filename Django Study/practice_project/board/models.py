from django.db import models

# Create your models here.
# 데이터베이스와 통신
class Question(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title