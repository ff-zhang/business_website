from django import forms

from .models import Club

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields =["name", "text"]

class EmailForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    email = forms.EmailField()

    # Choices is empty to avoid migration error
    options = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        club_names = [(club.name.lower(), club.name) for club in Club.objects.order_by("name")]
        super().__init__(*args, **kwargs)
        self.fields["options"].choices = club_names
