from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "business/index.html", context)

def clubs(request, club_name):
    context = {"club_name": club_name}
    return render(request, "business/clubs.html", context)

def sign_up(request):
    context = {}
    return render(request, "business/sign_up.html", context)