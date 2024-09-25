from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

app_name = "blog"


urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('blog/', views.PostList.as_view(), name='post-list'),
    path('blog/<int:pk>/', views.PostDetail().as_view(), name='post-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
])

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]