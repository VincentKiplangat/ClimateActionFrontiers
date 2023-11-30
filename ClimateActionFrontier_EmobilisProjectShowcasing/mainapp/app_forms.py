from django import forms

from mainapp.models import Donor


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = "__all__"
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date", "min": "1990-01-01", "max": "2005-12-31"}),
            "salary": forms.NumberInput(attrs={"max": 7500000000000000000, "min": 0})
        }
        labels = {
            "dob": "Date Of Birth",
            "email": "Email Address",
            "salary": 'Donation',
            "donor": "member"
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)

    # *************************************************************************


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
