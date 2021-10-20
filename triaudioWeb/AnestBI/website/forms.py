from .models import *
from django import forms
from django.forms import ModelForm
from website.models import usuario, paciente
from crispy_forms.helper import FormHelper
from django import forms
class usuariofrom(ModelForm):
    class Meta:
        model = usuario
        fields = ['nome','sobrenome','cpf','Telefone','Telefone2','cnes','Especialidade','registro','Registro_numero']
class pacienteform(ModelForm):
    class Meta:
        model = paciente
        fields=['nomeNeonato','sobreNeonato','sexo','Parto','apgar','apgar2','irda','obito','obs','nomeResponsavel','cpf_responsavel',
        'email_responsavel','Telefone_respnsavel','Telefone_respnsavel2','cep','Endereco','Numero','Bairro','cidade','uf','complemento']
    def __init__(self, *args, **kwargs):
        super(pacienteform,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False 
        self.fields['Numero'].required = False
        self.fields['complemento'].required =False