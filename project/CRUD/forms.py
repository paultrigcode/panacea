from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    song=forms.CharField(max_length=20)

    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password','song']


    def save(self):
        password=self.cleaned_data.pop('password')
        u=super().save()
        u.set_password(password)
        u.save()
        return u
