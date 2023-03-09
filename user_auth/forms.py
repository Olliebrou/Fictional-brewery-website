from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from datetime import date


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')
    birth_date = forms.DateField(
        label=_("Date of birth"),
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        help_text=_("You must be 18 years or older to register."),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'birth_date')

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        age = (date.today() - birth_date).days // 365
        if age < 18:
            raise forms.ValidationError(_("You must be 18 years or older to register."))
        return birth_date
