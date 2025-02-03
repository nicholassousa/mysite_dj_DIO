from django import forms
from .models import Contact


class NameForm(forms.Form):
    your_name = forms.CharField(label="Seu nome", max_length=100)

# este é o formulário que vai aparecer no navegador para ser preenchido pelo usuário


class ContactForm(forms.ModelForm): # usamos o ModelForm para criar um formulário baseado no modelo de dados
    class Meta:
        model = Contact
        fields = "__all__"

# este é o formulário que vai ser usado para cadastrar contatos no banco de dados.