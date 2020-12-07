from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Name',
        'class':"form-control"
    }))
    email=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your Email',
        'class':"form-control"
    }))
    phone=forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':'+91',
        'class':"form-control"
    }))
    subject=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Subject',
        'class':"form-control"
    }))
    message=forms.CharField(widget=forms.Textarea(attrs={
        'placeholder':'Message',
        'class':"form-control",
        'rows':5
    }))
