from django import forms


class ArticleComentatForm(forms.Form):
    file = forms.FileField(label="Selecciona un fitxer")

    def clean_file(self):
        return self.cleaned_data['file']
