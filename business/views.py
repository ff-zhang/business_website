from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail

from .models import Club
from .forms import EmailForm

# Create your views here.
def index(request):
    clubs = Club.objects.order_by("name")
    context = {"clubs": clubs}

    return render(request, "business/index.html", context)

def clubs(request):
    clubs = Club.objects.order_by("name")
    context = {"clubs": clubs}

    return render(request, "business/clubs.html", context)

def club(request, name):
    clubs = Club.objects.order_by("name")
    club = Club.objects.get(name=name)
    context = {"clubs": clubs, "club": club}

    return render(request, "business/club.html", context)

def sign_up(request):
    if request.method == "POST":
        form = EmailForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            chosen_clubs = form.cleaned_data["options"]
            recipient = form.cleaned_data["recipient"]
            
            message = first_name + " (" + recipient + ") wants to join:\n"
            for name in chosen_clubs:
                message += name + "\n"

            send_mail(
                "New Person Signed Up",
                message,
                settings.EMAIL_HOST_USER,
                [recipient],
                fail_silently=False,
            )

            return HttpResponseRedirect(reverse("business:index"))

    else:
        form = EmailForm()

    clubs = Club.objects.order_by("name")
    context = {"clubs": clubs, "form": form}

    return render(request, "business/sign_up.html", context)

def innovation_hub(request):
    clubs = Club.objects.order_by("name")
    context = {"clubs": clubs}

    return render(request, "business/innovation_hub.html", context)