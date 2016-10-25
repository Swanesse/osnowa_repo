from django import forms
from .models import Point
import re
from django import forms
from osnowa_app.models import User
from django.core.exceptions import ObjectDoesNotExist



class PointForm(forms.ModelForm):

    class Meta:
        model = Point
        fields = ('arkusz_mapy', 'nazwa', 'klasa','numer_katalogowy', 'wojewodztwo', 'powiat', 'gmina', 'miejscowosc', 'wsp_2000', 'wsp_lokalne', 'wsp_WGS84', 'h_amsterdam', 'h_kronsztadt_86', 'stabilizacja', 'zdjecie')


    # #Formularz logowania
    #     class FormularzLogowania(forms.Form):
    #         username = forms.CharField(label="Login:", max_length=30)
    #         password = forms.CharField(label="Hasło:", widget=forms.PasswordInput())
    #
    #         def clean_username(self):
    #             username = self.cleaned_data['username']
    #             try:
    #                 user = User.objects.get(username=username)
    #                 return username
    #             except ObjectDoesNotExist:
    #                 raise forms.ValidationError("Niepoprawny login")
    #
    #         def clean_password(self):
    #             if self.cleaned_data.has_key('username'):
    #                 username = self.cleaned_data['username']
    #                 password = self.cleaned_data['password']
    #                 user = User.objects.get(username=username)
    #                 if user.check_password(password):
    #                     return password
    #                 raise forms.ValidationError("Niepoprawne hasło")
    #             raise forms.ValidationError("Niepoprawny login")




    #Formularz rejestracji
class FormularzRejestracji(forms.Form):
    username = forms.CharField(label="Login:", max_length=30)
    email = forms.EmailField(label="Email:")
    password1 = forms.CharField(label="Hasło:", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Powtórz hasło:", widget=forms.PasswordInput())
    phone = forms.CharField(label="Telefon:", max_length=20, required=False)
    log_on = forms.BooleanField(label="Logowanie po rejestracji:", required=False)

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 == password2:
            return password2
        else:
            raise forms.ValidationError("Hasła się różnią")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Dopuszczalne są tylko cyfry, litery angielskie i _")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Taki użytkownik już istnieje")
