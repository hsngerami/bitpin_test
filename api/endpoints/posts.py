from django.urls import path

from api.routes.posts import PostListView

endpoints = [
    path('', PostListView.as_view(), name="posts_list"),
]
