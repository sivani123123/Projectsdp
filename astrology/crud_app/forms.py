# astrology/models.py
from django.db import models

# crud_app/forms.py
from django import forms
from .models import Prediction

class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ['title', 'description', 'date_predicted']
