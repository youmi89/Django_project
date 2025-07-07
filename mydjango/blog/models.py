from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
        """게시글 카테고리 모델"""
        name = models.CharField(max_length=100, unique=True, verbose_name="카테고리명")
        slug = models.SlugField(max_length=100, unique=True, verbose_name="슬러그")
        description = models.TextField(blank=True, verbose_name="설명")
        created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
        
        class Meta:
            verbose_name = "카테고리"
            verbose_name_plural = "카테고리 목록"
            ordering = ['name']

        def __str__(self):
            return self.name
        
class Tag(models.Model):
    """블로그 태그"""
    name = models.CharField(max_length=50, unique=True, verbose_name="태그명")
    slug = models.SlugField(max_length=50, unique=True, verbose_name="슬러그")  
    
    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그"
        ordering = ['name']   
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name='내용')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='작성일')
        # author = models.ForeignKey(User, on_delete=models.CASCADE)
        # title = models.CharField(max_length=100)
        
        # DB가 아니라, 장고 모델 단에서 생성/수정 시에 자동으로 시각을 입력함
        # created_at = models.DateTimeField(auto_now_add=True)
        # updated_at = models.DateTimeField(auto_now=True)
        # slug = models.SlugField(max_length=200, blank=True, null=True) #verbose_name="슬러그")
        # author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
        # category = models.ForeignKey('blog.Category', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="카테고리")
        # tags = models.ManyToManyField(Tag, blank=True, verbose_name="태그")
        # content = models.TextField(verbose_name="내용")
        # excerpt = models.TextField(max_length=300, blank=True, verbose_name="요약", help_text="게시글 요약 (미입력시 자동 생성)")
        # # featured_image = models.ImageField(upload_to='blog/images/', blank=True, null=True, verbose_name="대표 이미지")
        # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="상태")
        # is_featured = models.BooleanField(default=False, verbose_name="추천 게시글")
        # created_date = models.DateTimeField(default=timezone.now, verbose_name='작성일')
        # updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")
        # published_at = models.DateTimeField(blank=True, null=True, verbose_name="발행일")
        # views_count = models.PositiveIntegerField(default=0, verbose_name="조회수")
        
    class Meta:
            # ordering = ['-created_date']
            verbose_name = "게시글"
            verbose_name_plural = "게시글"
        
    def __str__(self):
            return self.title
    
def save(self, *args, **kwargs):
        # 발행 상태로 변경될 때 발행일 설정
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        
        # 요약이 없으면 내용에서 자동 생성
        if not self.excerpt and self.content:
            self.excerpt = self.content[:300] + '...' if len(self.content) > 300 else self.content
        
        super().save(*args, **kwargs)
    
def increment_views(self):
        """조회수 증가"""
        self.views_count += 1
        self.save(update_fields=['views_count'])

class Comment(models.Model):
    """댓글 (선택사항)"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name="게시글")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자")
    content = models.TextField(verbose_name="댓글 내용")
    is_active = models.BooleanField(default=True, verbose_name="활성화")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")
    
    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.post.title}의 댓글 - {self.author.username}"