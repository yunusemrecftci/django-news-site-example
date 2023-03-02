from django.urls import path
from .views import *

urlpatterns = [
    path("",indexpage,name="indexpage"),
    path("post",postpage,name="postpage"),
    path("post/<slug>",detailpage,name="postdetail"),
]
