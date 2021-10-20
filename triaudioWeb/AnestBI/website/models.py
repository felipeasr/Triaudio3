from django.db import models


# Register your models here.

# Create your models here.
# Register your models here.

# Create your models here.
class usuario (models.Model):
    """Model representing an usuario."""
    REGISTRO_CONSELHO =(
        ("CRM","CRM"),
        ("CRFa","CRFa"),
        ("CREFITO","CREFITO"),
        ("COREN","COREN"),
        ("CRP","CRP"),
        ("CRAS","CRAS"),
        ("CRO","CRO"),
        ("Outros","Outros"),

    )

    nome = models.CharField(max_length=100, null=False, verbose_name="Nome")
    cpf = models.CharField(max_length=14,null=False,verbose_name="CPF")
    sobrenome = models.CharField(max_length=100, null=False, verbose_name="Sobrenome")
    Telefone = models.CharField(max_length=15, null=False, verbose_name="Telefone")
    Telefone2 = models.CharField(max_length=15, null=False, verbose_name="Telefone2")
    cnes = models.CharField(max_length=100, null=False, verbose_name="CNES ou CNPJ")
    Especialidade= models.CharField(max_length=100, null=False, verbose_name="Especialidade ")
    registro=models.CharField(null=False,choices=REGISTRO_CONSELHO,max_length=15)
    Registro_numero= models.CharField(max_length=100, null=False, verbose_name="Registro")
   
    class Meta:
        ordering = ['cpf', 'nome']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('usuario-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.cpf}, {self.nome}'

class paciente (models.Model):
    PARTO_RADIO=(
        ("Normal","Normal"),
        ("Cesárea","Cesárea"),
    )
    SEXO_RADIO=(
        ("Masculino","Masculino"),
        ("Feminino","Feminino"),
    )
    IRDA_RADIO=(
        ("Sim","Sim"),
        ("Não","Não"),
    )
    APGAR_RADIO=(
        ("1 APGAR","1 APGAR"),
        ("2 APGAR","2 APGAR"),
        ("3 APGAR","3 APGAR"),
        ("4 APGAR","4 APGAR"),
        ("5 APGAR","5 APGAR"),
        ("6 APGAR","6 APGAR"),
        ("7 APGAR","7 APGAR"),
        ("8 APGAR","8 APGAR"),
        ("9 APGAR","9 APGAR"),
        ("10 APGAR","10 APGAR"),
    )
    APGAR_RADIO2=(
        ("1 APGAR","1 APGAR"),
        ("2 APGAR","2 APGAR"),
        ("3 APGAR","3 APGAR"),
        ("4 APGAR","4 APGAR"),
        ("5 APGAR","5 APGAR"),
        ("6 APGAR","6 APGAR"),
        ("7 APGAR","7 APGAR"),
        ("8 APGAR","8 APGAR"),
        ("9 APGAR","9 APGAR"),
        ("10 APGAR","10 APGAR"),
    )
    nomeNeonato = models.CharField(max_length=100, null=False, verbose_name="Nome")
    sobreNeonato = models.CharField(max_length=100, null=False, verbose_name="Sobrenome")
    Parto = models.CharField(null=False,choices=PARTO_RADIO,max_length=15,verbose_name="Tipo de Parto")
    sexo = models.CharField(null=False,choices=SEXO_RADIO,max_length=15)
    apgar=models.CharField(null=False,choices=APGAR_RADIO,max_length=15)
    apgar2=models.CharField(null=False,choices=APGAR_RADIO2,max_length=15)
    irda=models.CharField(null=False,choices=IRDA_RADIO,max_length=15)
    obito=models.CharField(max_length=6,verbose_name="òbito")
    obs=models.CharField(max_length=100000)
    nomeResponsavel=models.CharField(max_length=100, null=False, verbose_name="Nome do Responsavel")
    cpf_responsavel=models.CharField(max_length=14,null=False,verbose_name="CPF Responsavel")
    email_responsavel = models.EmailField(max_length=100,null=False,verbose_name="Email do Responsavel")
    Telefone_respnsavel=models.CharField(max_length=15, null=False, verbose_name="Telefone")
    Telefone_respnsavel2=models.CharField(max_length=15, null=False, verbose_name="Telefone")
    cep=models.CharField(max_length=10, null=False)
    Endereco=models.CharField(max_length=150, null=False)
    Numero=models.CharField(max_length=150, null=False)
    Bairro=models.CharField(max_length=150, null=False)
    cidade=models.CharField(max_length=150, null=False)
    uf=models.CharField(max_length=150, null=False)
    complemento=models.CharField(max_length=150, null=False)
    class Meta:
        ordering = ['nomeNeonato']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('paciente-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f' {self.nomeNeonato}'