from django.forms import ModelForm
from .models import feedbackModel 

class feedbackForm(ModelForm):
    class Meta:
        model = feedbackModel
        fields='__all__'

