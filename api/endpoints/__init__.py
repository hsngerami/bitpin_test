from django.contrib import admin
from django.urls import path, include
from api.endpoints import posts, rates

urlpatterns = [
    path('posts/', include(posts.endpoints)),
    path('rates/', include(posts.endpoints))
]
