from django import forms


class ValutazioneForm(forms.Form):
    voto_brano = forms.FloatField(min_value=0, max_value=10)
    voto_interpretazione = forms.FloatField(min_value=0, max_value=10)
    voto_outfit = forms.FloatField(min_value=0, max_value=10)

    def __init__(self, *args, **kwargs):
        self.voto_brano = kwargs.pop('voto_brano', None)
        self.voto_interpretazione = kwargs.pop('voto_interpretazione', None)
        self.voto_outfit = kwargs.pop('voto_outfit', None)

        kwargs.update(initial={
            'voto_brano': self.voto_brano,
            'voto_interpretazione': self.voto_interpretazione,
            'voto_outfit': self.voto_outfit
        })

        super().__init__(*args, **kwargs)


class RegistratiForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    conferma_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    cognome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
