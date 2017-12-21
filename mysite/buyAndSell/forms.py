from django import forms

class buyAndSellForm(forms.Form):
    Limit = forms.CharField(label='Limit', max_length=100)
    Price = forms.CharField(label='price', max_length=100)
    Amount = forms.CharField(label='amount', max_length=100)
     