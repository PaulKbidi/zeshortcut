from django import forms

SEX_CHOICES = {
    "0": "Homme",
    "1": "Femme",
}
class InfoForm(forms.Form):
    sex = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=SEX_CHOICES,
    )
    age = forms.CharField(
        max_length=32,
        widget=forms.NumberInput(attrs={'placeholder':'Âge'})
    )
    size = forms.CharField(
        max_length=100,
        widget=forms.NumberInput(attrs={'placeholder':'Taille'})
    )
    weight = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': 'Poids'})
    )