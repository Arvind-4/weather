from django import forms


class WeatherForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter a Valid Place ...",
                "class": "form-control",
            }
        ),
    )
