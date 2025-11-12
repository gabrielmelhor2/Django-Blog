from django.urls import path, include
from .views import *

urlpatterns = [
    path("", posts_view, name="posts_view"),
    path('new_post/', new_post, name='new_post'),
]
