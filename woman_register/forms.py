from django import forms
from .models import Woman

class WomanForm(forms.ModelForm):

    class Meta:
        model = Woman
        fields = '__all__'
        labels = {
            'wom_code':'Descreva um ponto de referência próximo da ocorrência(Ex: Supermercado, Farmácias)',
            'descricao':'Descrição',
            'numero':'Telefone',
            'cpf':'CPF',

        }