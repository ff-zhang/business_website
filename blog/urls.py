"""Defines URL patterns for blog."""

from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    # Home page.
    path("", views.index, name="index"),

    # Detail page for a single topic.
    path("topics/<int:topic_id>/", views.topic, name="topic"),

    path("user/<int:user_id>/", views.user_posts, name="user_posts"),

    # Page for adding a new post from the home page.
    path("new_post/", views.new_post, name="new_post"),

    # Page for adding a new post from a topic page.
    path("new_post/<int:topic_id>/", views.new_post, name="new_post"),

    # Page for editing an post.
    path("edit_post/<int:post_id>/", views.edit_post, name="edit_post"),
]