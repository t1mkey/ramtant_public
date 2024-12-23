from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

from users.models import Usr, Profile

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  
        model = User

class ProfileEditing(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'bio', 'img' ]    