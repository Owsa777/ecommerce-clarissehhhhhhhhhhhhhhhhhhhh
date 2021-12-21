from django import forms

class ContactForm(forms.Form):
    nombre =  forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {
    'placeholder': "Nombre"
    }))
    email =  forms.CharField(widget = forms.TextInput(attrs = {
    'placeholder': "Email"
    }))
    mensaje =  forms.CharField(widget = forms.TextInput(attrs = {
    'placeholder': "Comentario"
    }))
