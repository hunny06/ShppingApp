from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.models import User
from .models import Customer

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class":"form-control"}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={"class":"form-control"}))
    class Meta:
        model = User
        fields = ['username','password1','password2','email']
        labels = {"email":"Email"}
        widgets = {"username":forms.TextInput(attrs={"class":'form-control'})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus":True,"class":"form-control"}))
    password = forms.CharField(label = _("Password"),widget=forms.PasswordInput(attrs={"autocomplete":"current-password","class":"form-control"}))

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label = _("Old Password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":"current-password","autofocus":True,"class":"form-control"}))
    new_password1 = forms.CharField(label = _("New Password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":"new-password","class":"form-control"}))
    new_password2 = forms.CharField(label= _("Confirm Password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":"new-password","class":"form-control"}))

class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(label = _("Email"), max_length=245, widget=forms.EmailInput(attrs={"autocomplete":"email","class":"form-control"}))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label = _("New Password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":"new-password","class":"form-control"}))
    new_password2 = forms.CharField(label= _("Confirm Password"),strip=False,widget=forms.PasswordInput(attrs={"autocomplete":"new-password","class":"form-control"}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name","locality","city","zipcode","state"]
        widget = {"name":forms.TextInput(attrs={"class":'form-control',"placeholder":"Name"}),
        "locality":forms.TextInput(attrs={"class":"form-control","placeholder":"Locality"}),
        "city":forms.TextInput(attrs={"class":"form-control","placeholder":"City"}),
        "zipcode":forms.NumberInput(attrs={"class":"form-control","placeholder":"ZipCode"}),
        "state":forms.Select(attrs={"class":"form-control","placeholder":"State"}),
        }