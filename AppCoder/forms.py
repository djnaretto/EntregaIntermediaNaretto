from django import forms

class GerenciaFormulario(forms.Form):
    nombre = forms.CharField()
    n_integrantes = forms.IntegerField()

class GerenteFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    gerencia= forms.CharField(max_length=30)

class ColaboradorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    cargo= forms.CharField(max_length=30)