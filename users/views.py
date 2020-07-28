from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import views as auth_views, login, authenticate, logout, models
from django.shortcuts import render

from random import randint

from blog.models import Topic
from business.models import Club
from .forms import SignUpForm

# Create your views here.
class LoginView(auth_views.LoginView):
    """Log the user in."""
    template_name = "users/login.html"

    topics = Topic.objects.order_by("text")
    clubs = Club.objects.order_by("name")
    extra_context = {"topics": topics, "clubs": clubs}

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.username = form.cleaned_data["email"]
            user.save()

            blog_group = models.Group.objects.get(name="blog")
            blog_group.user_set.add(user)

            user = authenticate(username=user.username, password=form.cleaned_data["password1"])
            login(request, user)

            return HttpResponseRedirect(reverse("blog:index"))

    else:
        form = SignUpForm()

    topics = Topic.objects.order_by("text")
    clubs = Club.objects.order_by("name")
    context = {"topics": topics, "clubs": clubs, "form": form}

    return render(request, "users/sign_up.html", context)

def log_out(request):
    """Log the user out."""
    logout(request)

    return HttpResponseRedirect(reverse("blog:index"))