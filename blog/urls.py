from django.urls import path, include

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/", views.detail, name="detail"),
    path('post_thumbsup/<int:pk>/', views.post_thumbsup, name="thumbsup"),
    path('post_thumbsdown/<int:pk>/', views.post_thumbsdown, name="thumbsdown"),
    path('tag/<tag>', views.TagListView.as_view(), name='tag'),
]