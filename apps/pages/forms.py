from django import forms
from apps.core.models import Session

class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = ["description", "allow_observers"]