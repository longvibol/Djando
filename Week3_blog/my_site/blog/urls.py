from django.urls import path
from . import views

urlpatterns = [
    path("",views.starting_page, name="starting-page"),  # root URL
    path("posts",views.posts, name="posts-page"),      # static URL for posts listing
    path("post/<str:slug>", views.post_detail, name="post-detail-page"), # dynamic URL segment for post slug ex: post/my-first-post
]
