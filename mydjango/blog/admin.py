from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']  # 목록에서 보여줄 필드
    list_filter = ['created_date']  # 필터 옵션
    search_fields = ['title', 'content']  # 검색 필드
    date_hierarchy = 'created_date'  # 날짜별 계층 구조
    ordering = ['-created_date']  # 정렬 순서