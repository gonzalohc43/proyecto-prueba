from django import  forms


class Registro(forms.Form):
  username= forms.CharField(required=True, min_length=4, max_length=60,widget=forms.TextInput(attrs={
    'class': 'form-control',
    'id': 'Id',
    'placeholder': 'username'
  }))
  email= forms.EmailField(required=True,widget=forms.EmailInput(attrs={
    'class': 'form-control',
    'id' : 'email',
    'placeholder' : 'email'
  }))
  password=forms.CharField(required=True,widget=forms.PasswordInput(attrs={
    'class': 'form-control',
    'placeholder' : 'Password'
  }))