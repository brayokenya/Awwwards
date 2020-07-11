from .models import Site
from django import forms


class NewSiteForm(forms.ModelForm):
    class Meta:
        model = Site
        exclude = ['developer', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
