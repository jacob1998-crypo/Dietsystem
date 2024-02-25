# userprofile/forms.py

# forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'gender', 'weight_kg', 'height_ft','conditions', 'preferences']

