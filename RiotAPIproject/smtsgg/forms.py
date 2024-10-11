from django import forms

class NameForm(forms.Form):
    name_and_tag = forms.CharField()