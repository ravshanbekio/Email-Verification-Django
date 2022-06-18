from account.models import Account
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('first_name','last_name','username','email','proffession', 'password1', 'password2')
        labels = {
            'first_name': '',
            'last_name': '',
            'username':'',
            'email': '',
            'proffession': '',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control','name':'first_name','placeholder':'First name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','name':'last_name','placeholder':'Last name'}),
            'username': forms.TextInput(attrs={'class':'form-control','name':'username','placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control','name':'email','placeholder':'Email Address'}),
            'proffession': forms.Select(attrs={'class':'form-control','name':'proffession','placeholder':'Proffession'})
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'