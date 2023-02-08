from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 


class CreateUserForm(UserCreationForm): 
    def clean_email(self):
        data = self.cleaned_data['email']
        if data.split('@')[1] != "cear.ufpb.br":   
            raise forms.ValidationError("Necessário que o email seja do domínio @cear.")
        return data
    class Meta: 
        model = User
        fields = ['username', 'email', 'password1', 'password2']