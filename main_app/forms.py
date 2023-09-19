from django.forms import ModelForm
from .models import Review, Day

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review']

class DayForm(ModelForm):
    class Meta:
        model = Day
        fields = ['days', 'opening_time', 'closing_time', 'opening_hours', 'closing_hours']
