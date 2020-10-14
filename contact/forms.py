from django import forms

class feedsForm(forms.Form):
    fullname = forms.CharField(
            max_length=70,
            widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Full Name"
                })
            )
    mailAddr = forms.CharField(
            max_length=70,
            widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Your Email Address..."
                })
            )
    company = forms.CharField(
            max_length=100,
            widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Company"
                })
            )
    body = forms.CharField(
            widget=forms.Textarea(attrs={
                "class":"form-control",
                "placeholder":"Your Feedback..."
                })
            )

class newsletterForm(forms.Form):
    mail = forms.CharField(
            max_length = 70,
            widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Email Address"
                })
            )
