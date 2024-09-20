from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

app_name = "blog"

urlpatterns = [
    path('blog/', views.PostList.as_view()),
    path('blog/<int:pk>/', views.PostDetail().as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

