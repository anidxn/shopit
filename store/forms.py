from django import forms
# ---- built in forms-----
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#==============================================
# REF: User-Authentication Application
#=============================================

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'something@django.com'}))
    first_name = forms.CharField(max_length=50, 
                                 widget=forms.TextInput(attrs={'class': 'form-control' }))
    last_name = forms.CharField(max_length=50, 
                                widget=forms.TextInput(attrs={'class': 'form-control' }))

    class Meta:  
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

        

    # following is required to decorate the 3 default fiels of UserCreationForm e.g. username, password1 & password2

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Your username'
        self.fields['username'].label = 'User_name'
        self.fields['username'].help_text = "<span class='form-text text-muted'><small>Required. maximum 50 characters allowed with letter, digits and @/./+/-/_<small><span>"

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class ProfileUpdateForm:
    pass