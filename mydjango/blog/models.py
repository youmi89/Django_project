from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    # DB가 아니라, 장고 모델 단에서 생성/수정 시에 자동으로 시각을 입력함
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)