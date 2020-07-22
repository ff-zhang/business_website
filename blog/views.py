from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from business.models import Club
from .models import Topic, Post
from .forms import TopicForm, PostForm

# Create your views here.
def index(request):
    """The home page for the blog."""
    topics = Topic.objects.order_by("text")
    posts = Post.objects.order_by("date_added").reverse()
    clubs = Club.objects.order_by("name")
    context = {"topics": topics, "posts": posts, "clubs": clubs}

    return render(request, "blog/index.html", context)

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by("text")
    clubs = Club.objects.order_by("name")
    context = {"topics": topics, "clubs": clubs}

    return render(request, "blog/topics.html", context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topics = Topic.objects.order_by("text")
    topic = Topic.objects.get(id=topic_id)
    posts = topic.post_set.order_by("date_added").reverse()
    clubs = Club.objects.order_by("name")
    context = {"topics": topics, "topic": topic, "posts": posts, "clubs": clubs}

    return render(request, "blog/topic.html", context)

@login_required()
def new_topic(request):
    """Add a new topic."""
    topics = Topic.objects.order_by("text")
    clubs = Club.objects.order_by("name")

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("blog:home"))

    context = {"topics": topics, "form": form, "clubs": clubs}

    return render(request, "blog/new_topic.html", context)

@login_required
def new_post(request, topic_id=None):
    """Add a new post for a particular topic."""
    topics = Topic.objects.order_by("text")
    clubs = Club.objects.order_by("name")

    if topic_id:
        topic = Topic.objects.get(id=topic_id)
    else:
        topic = None

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = PostForm(initial={"topic": topic})
    else:
        # POST data submitted; process data.
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save()
            if topic_id:
                return HttpResponseRedirect(reverse("blog:topic", args=[topic_id]))
            else:
                return HttpResponseRedirect(reverse("blog:home"))

    context = {"topics": topics, "topic": topic, "form": form, "clubs": clubs}

    return render(request, "blog/new_post.html", context)

@login_required
def edit_post(request, post_id):
    """Edit an existing post."""
    topics = Topic.objects.order_by("text")
    post = Post.objects.get(id=post_id)
    clubs = Club.objects.order_by("name")

    if request.method != "POST":
        # Initial request; pre-fill form with the current post.
        form = PostForm(instance=post)
    else:
        # POST data is submitted; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("blog:home"))

    context = {"topics": topics, "post": post, "form": form, "clubs": clubs}

    return render(request, "blog/edit_post.html", context)
