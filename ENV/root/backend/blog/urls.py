"""Script holds all url mappings for the blog django app.
"""
from django.urls import path

from blog.views.blogviews import HeadingsView
from blog.views.postviews import (
    PostView,
    PublishView,
    DraftView
)

urlpatterns = [
    path('headings/<int:days>/', HeadingsView.as_view()),
    path('draft/', DraftView.as_view()),
    path('publish/', PublishView.as_view()),
    path('post/<str:slug>/', PostView.as_view()),
]
