from django import forms 
from .models import ContactForm
from django.contrib.auth.models import User


class ContactDataForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=65, label= 'Nombre')
    message = forms.CharField(label='Mensaje', widget=forms.Textarea)
    
class ContactDataModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email', 'password', 'first_name', 'last_name']
