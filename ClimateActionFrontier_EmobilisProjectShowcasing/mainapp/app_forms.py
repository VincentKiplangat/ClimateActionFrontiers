from django import forms

from mainapp.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date", "min": "1990-01-01", "max": "2005-12-31"}),
            "salary": forms.NumberInput(attrs={"max": 7500000000000000000, "min": 0})
        }
        labels = {
            "dob": "Date Of Birth",
            "email": "Email Address",
            "salary": 'Donation',
        }


class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)
