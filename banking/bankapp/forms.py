from django import forms
from .models import Application,User_Table
from django import forms
from django.contrib.auth.forms import UserCreationForm



class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'

    name = forms.CharField(max_length=100)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], widget=forms.RadioSelect)
    phone_number = forms.CharField(max_length=15)
    mail_id = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    district = forms.ChoiceField(choices=[('Calicut', 'Calicut'), ('Wayanad', 'Wayanad'), ('Thrissur', 'Thrissur'),('Palakkad','Palakkad'),('Kannur','Kannur')])  # Initial district choices
    branch = forms.ChoiceField(choices=[('default', '---------')])  # Default branch choice
    account_type = forms.ChoiceField(choices=[('Savings', 'Savings Account'), ('Current', 'Current Account')])
    materials_provide = forms.MultipleChoiceField(
        choices=[('debit_card', 'Debit Card'), ('credit_card', 'Credit Card'), ('cheque_book', 'Cheque Book')],
        widget=forms.CheckboxSelectMultiple
    )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User_Table # Replace 'User' with your custom user model if you have one
        fields = ('username', 'email', 'password1', 'password2')
