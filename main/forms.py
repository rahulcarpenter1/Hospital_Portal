from django import forms
from .models import Crud

class CrudForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Enter Patient Name...",
        "class": "form-control"
    }))

    casechoice = [
        ("", '-------'),
        ("General Physician", "General Physician"),
        ("Surgeon", "Surgeon"),
        ("Pediatrician", "Pediatrician"),
        ("Gynecologist", "Gynecologist"),
        ("Cardiologist", "Cardiologist"),
        ("Neurologist", "Neurologist"),
    ]
    case = forms.ChoiceField(
        choices=casechoice,
        label="Case",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    refer = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Referred by...",
            "class": "form-control"
        })
    )

    schemechoice = [
        ("","----"),
        ("Ayushman","Ayushman"),
        ("None","None"),
    ]
    scheme = forms.ChoiceField(
        choices=schemechoice,
        label="Scheme",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    statuschoice = [
        ("","----"),
        ("Admit","Admit"),
        ("Discharge","Discharge"),
    ]
    status = forms.ChoiceField(
        choices=statuschoice,
        label="Status",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = Crud
        fields = ["name", "case", "refer", "scheme", "status"]
