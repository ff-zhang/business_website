from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Topic, Post

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["topic", "title", "text"]
        labels = {"topic": "" , "title": "",  "text": ""}
