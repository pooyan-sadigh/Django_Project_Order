from django import forms
import datetime
from warehouse.models import warehouse

All = warehouse.objects.all()
Choices = []
for x in All:
    a = (x, x)
    Choices.append(a)


class input_beta(forms.Form):
    ware = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),
                             choices=Choices)

    shrinks = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'no of shrinks'}), max_value=20,
        min_value=1)

    date = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Date of arrival')

    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'id': 'comment',
                                     'placeholder': 'country, state, city, ...'}))

    def clean_date(self):
        Date = self.cleaned_data.get('date')
        now = datetime.date.today()
        days = (Date - now).days
        if days < 0:
            raise forms.ValidationError('incorrect date!')
        elif days < 7:
            raise forms.ValidationError('minimum delivery time is 7 days')
        elif days > 30:
            raise forms.ValidationError('orders for more than 30 days are not acceptable')
        return days
