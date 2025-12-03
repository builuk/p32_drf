from django.urls import path, re_path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    re_path(r'^posts/(?P<pk>\d+)/?$', views.post_detail, name='post_detail'),
    path('comments/', views.comment_list, name='post_list'),
    re_path(r'^comments/(?P<pk>\d+)/?$', views.comment_detail, name='post_detail'),
    path('time-info/', views.time_info, name='time-info'),
    path('greeting/', views.greeting, name='greeting'),
    path('math/', views.math_operations, name='math-operations'),
    # path('power/', views.power_operations, name='power-operations'),
]
