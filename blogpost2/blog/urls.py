from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

app_name = "blog"

urlpatterns = [
    path('blog/', views.post_list),
    path('blog/<int:pk>/', views.post_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)

