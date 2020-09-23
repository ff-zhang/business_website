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
            chosen_clubs = [club.title() for club in form.cleaned_data["options"]]
            email = form.cleaned_data["email"]
            
            message = first_name + " (" + email + ") wants to join:\n"
            for name in chosen_clubs:
                message += name + "\n"

            # Send email to business club
            send_mail(
                "New Member Signed Up",
                message,
                settings.CLUB_EMAIL,
                [settings.CLUB_EMAIL],
                fail_silently=False,
            )

            # Send email to the requestee
            message = "Thank you for signing up for "

            if len(chosen_clubs) == 1:
                message += chosen_clubs[0] + "."

            else:
                for i in range(len(chosen_clubs) - 1):
                    message += chosen_clubs[i] + ", "

                message += "and " + chosen_clubs[-1] + "."

            send_mail(
                "Thank You for Signing Up",
                message,
                settings.CLUB_EMAIL,
                [email],
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