from django.urls import path
from .views import fnct_blog_home

app_name = 'ecomm'

urlpatterns = [
    path('', fnct_blog_home, name="url_blog_home"),
]
