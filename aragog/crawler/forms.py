from django import forms


class UrlGatherer(forms.Form):
    url = forms.CharField(label='url', max_length=100)
