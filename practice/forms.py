from django import forms

class userForms(forms.Form):
    fname=forms.CharField(required=True,label="fname")
    lname=forms.CharField(required=True,label="lname")
    email=forms.EmailField(required=False)
    boollean=forms.BooleanField(label="boolena name")
    