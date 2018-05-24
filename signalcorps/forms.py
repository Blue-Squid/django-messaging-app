from django import forms

class MessagePost(forms.Form):
    post = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Go to the link above and encrypt message and paste it here.'}))