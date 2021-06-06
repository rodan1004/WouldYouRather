from django import forms


class QueryForm(forms.Form):
    Title = forms.CharField(max_length=200)
    Query1 = forms.CharField(max_length=200)
    Query2 = forms.CharField(max_length=200)
    Image1 = forms.ImageField()
    Image2 = forms.ImageField()