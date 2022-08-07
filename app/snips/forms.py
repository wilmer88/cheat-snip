from dataclasses import field
from django import forms
from snips.models import Snipit


class SnipitForm(forms.ModelForm):
    class Meta:
        model=Snipit
        fields = ["language_name","snip_title","language_code","short_description"]
 