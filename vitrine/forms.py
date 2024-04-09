from django import forms

SEX_CHOICES = {
    "0": "Homme",
    "1": "Femme",
}
class BmrForm(forms.Form):
    sex = forms.ChoiceField(
        label='Quel est votre sex ?',
        widget=forms.RadioSelect,
        choices=SEX_CHOICES,
    )
    age = forms.CharField(
        max_length=32,
        label='Quel âge avez-vous ?',
        widget=forms.NumberInput(attrs={'placeholder':'Âge'})
    )
    weight = forms.CharField(
        label='Combien pesez-vous ?',
        widget=forms.NumberInput(attrs={'placeholder': 'Poids'})
    )
    size = forms.CharField(
        max_length=100,
        label='Combien mesurez-vous ?',
        widget=forms.NumberInput(attrs={'placeholder':'Taille'})
    )
    
    
TYPE_PLAN = {
    "0": "prendre_du_poids",
    "1": "perdre_du_poids",
}
class PlanForm(forms.Form):
    typePlan = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=TYPE_PLAN,
    )
    userMail = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )