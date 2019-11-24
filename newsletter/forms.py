from django import forms
from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()
    
    # def clean_email(self):
    #     # print (self.cleaned_data)
    #     email = self.cleaned_data.get('email')
    #     _, provider = email.split('@')
    #     _, extension = provider.split('.')
    #     if not extension == 'edu':
    #         raise forms.ValidationError("Please use a valid college email address")
    #     return email


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']
        # exclude = ['full_name']

    # def clean_email(self):
    #     # print (self.cleaned_data)
    #     email = self.cleaned_data.get('email')
    #     _, provider = email.split('@')
    #     _, extension = provider.split('.')
    #     if not extension == 'edu':
    #         raise forms.ValidationError("Please use a valid college email address")
    #     return email