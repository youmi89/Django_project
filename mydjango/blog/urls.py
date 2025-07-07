from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path("write/", views.post_new),

    path('admin/', admin.site.urls),

    path('', views.post_list, name='post_list'),

    # path("<int:id>/", views.post_detail),

    # path("search/<str:tag>/", views.post_search),

    # path("edit/<int:id>/", views.post_edit),

    # path("delete/<int:id>/", views.post_delete),

    path('login/', views.login_page, name='login'),

    path('logout/', views.logout_page, name='logout'),

    path('post/new/', views.post_new, name='post_new'),

    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]