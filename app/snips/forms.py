from django import forms


class SnipitForm(forms.Form):
 
 language_name = forms.CharField(max_length=100)
 snip_title= forms.CharField(max_length=100)
 language_code= forms.CharField(max_length=3000)
short_description= forms.CharField(max_length=100)