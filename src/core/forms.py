from django import forms

class ContactForm(forms.Form):
    name =  forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {
    'placeholder': "Nombre"
    }))
    email =  forms.CharField(widget = forms.TextInput(attrs = {
    'placeholder': "Email"
    }))
    message =  forms.CharField(widget = forms.TextInput(attrs = {
    'placeholder': "Comentario"
    }))
