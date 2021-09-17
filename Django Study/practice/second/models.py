from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True) # 생설될 때 마다 나오는 시간
    updated_at = models.DateTimeField(auto_now=True) # 수정될 때 마다 넣는 것