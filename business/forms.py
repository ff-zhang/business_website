from django import forms

from .models import Club

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields =["name", "text"]

class EmailForm(forms.Form):
    club_names = [(club.name.lower(), club.name) for club in Club.objects.order_by("name")]

    first_name = forms.CharField(max_length=20)
    recipient = forms.EmailField()
    options = forms.MultipleChoiceField(choices=club_names, widget=forms.CheckboxSelectMultiple)
