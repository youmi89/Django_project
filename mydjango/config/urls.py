from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def root(request):
    return render(request, 'root.html')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),

    path('', root),
]
