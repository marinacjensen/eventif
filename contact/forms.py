from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nome:")
    email = forms.EmailField(label="E-mail:")
    phone = forms.CharField(label="Telefone:", required=False)
    message = forms.CharField(label="Mensagem:", widget=forms.Textarea)