from .models import Comment
from django import forms


class commentform(forms.ModelForm):
    class Meta:
        model= Comment
        fields=('name','email','body')




class contactform(forms.Form):
    name=forms.CharField(min_length=10,widget=forms.TextInput(attrs={'placeholder':'Your name'}))
    email=forms.EmailField(widget=forms.TextInput)
    message = forms.CharField(widget=forms.Textarea(attrs={'placehcdolder':'Your message here'}))