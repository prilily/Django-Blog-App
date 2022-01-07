from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView



urlpatterns=[
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'),
    path('about/',views.about,name='blog-about'), # this about is in the url after home page so do home/about
]

#blog/post_list.html  template with the name
# <app>/<model>_<view_type>.html blog/post_list.html
#so, change it in views.py


# route to specific f+post
'''blog/

url with variable like post/1 orpost/2
so id of post part of the route,
post/<int:pk>

pk is post we want to view and say what kind of variable it is

now a template for post details
with convention as <app>/<model>_<viewtype> i.e blog/post_detail.html
'''