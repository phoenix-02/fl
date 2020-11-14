from django import forms


class ProjectForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=500)
    price = forms.IntegerField()
