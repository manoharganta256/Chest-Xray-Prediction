from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from fusion.models import Profile,Image,UserProfile
from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','location','birth_date')
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('user','chest_xray')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user','profile_picture','limit')