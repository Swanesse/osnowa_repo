from django import forms
from .models import Point

class PointForm(forms.ModelForm):

    class Meta:
        model = Point
        fields = ('arkusz_mapy', 'nazwa', 'klasa','numer', 'wojewodztwo', 'powiat', 'gmina', 'miejscowosc', 'stabilizacja')
