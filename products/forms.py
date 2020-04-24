from django import forms

from .models import Product
from events.models import Event
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProductForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs= {
            'class': 'form-control',
            'placeholder': 'Title'
        }
    ))
    description = forms.CharField(required=True, widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }
        ))
    price = forms.DecimalField(required=True)
    image = forms.ImageField(required=False)
    sold_at = forms.ModelChoiceField(queryset = Event.objects.all() , required=False)
    daily_deal = forms.BooleanField(required=False)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit','Submit',css_class='btn-primary'))
